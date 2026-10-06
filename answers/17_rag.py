"""
Answers for 17_rag - try the questions first!

Every answer below is runnable code, so you can execute this file
and see each output for yourself.
"""

import numpy as np


# ------------------------------------------------------------------
# embeddings.py
# ------------------------------------------------------------------
# Q1: Identical vectors -> 1.0, always: dot(v, v) = |v| * |v|, so
#     cosine is |v|^2 / |v|^2 = 1 for ANY nonzero v (length cancels
#     out). Two vectors with no shared words have dot product 0, so
#     the score is 0.0.

def tokenize(text):
    return text.lower().replace("?", "").replace(".", "").split()


VOCAB = {"cat": 0, "chases": 1, "dog": 2, "mouse": 3}


def embed(text, vocab):
    vec = np.zeros(len(vocab))
    for word in tokenize(text):
        if word in vocab:
            vec[vocab[word]] = 1.0
    return vec


def cosine_similarity(a, b):
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    return 0.0 if denom == 0 else float(np.dot(a, b) / denom)


a = embed("dog chases", VOCAB)
print("emb Q1 -> identical:", round(cosine_similarity(a, a), 6),
      "| disjoint:", cosine_similarity(a, embed("cat mouse", VOCAB)))
# -> identical: 1.0 | disjoint: 0.0

# Q2: Without the guard, denom is 0.0 and numpy computes 0 / 0 --
#     not an exception but nan (plus a RuntimeWarning). nan poisons
#     the ranking silently: every comparison with nan is False, so
#     sorts become arbitrary. The guard returns the honest score
#     for "nothing known": 0.0.
zero_vec = np.zeros(4)
with np.errstate(invalid="ignore"):
    bad = np.dot(zero_vec, zero_vec) / (np.linalg.norm(zero_vec) ** 2)
print("emb Q2 -> without guard:", bad, "| with guard: 0.0")
# -> without guard: nan | with guard: 0.0

# Q3: embed_counts adds 1 per occurrence instead of capping at 1.0.
#     "dog dog cat" vs "dog cat": binary vectors are IDENTICAL
#     (presence, not amount) -> 1.0; count vectors differ ->
#     0.949. Counts only matter when repetition carries signal
#     (longer keyword-style text); for short sentences binary is
#     enough.


def embed_counts(text, vocab):
    vec = np.zeros(len(vocab))
    for word in tokenize(text):
        if word in vocab:
            vec[vocab[word]] += 1.0
    return vec


b1, b2 = embed("dog dog cat", VOCAB), embed("dog cat", VOCAB)
c1, c2 = embed_counts("dog dog cat", VOCAB), embed_counts("dog cat", VOCAB)
print("emb Q3 -> binary:", round(cosine_similarity(b1, b2), 3),
      "| counts:", round(cosine_similarity(c1, c2), 3))
# -> binary: 1.0 | counts: 0.949


# ------------------------------------------------------------------
# semantic_search.py
# ------------------------------------------------------------------
# Q1: keyword_search demands the WHOLE query verbatim inside a doc;
#     no FAQ repeats "how do i get my money back", so it finds
#     nothing. search() compares word slots: the query shares
#     "money" and "back" with the refund doc -> 0.378, rank 1.
#     (A trained model would also match "cash returned": zero
#     shared words, same meaning.)


def build_vocab(corpus):
    words = sorted({w for doc in corpus for w in tokenize(doc)})
    return {word: idx for idx, word in enumerate(words)}


FAQ = [
    "Full refund within 30 days: your money goes back to the "
    "original payment method.",
    "Reset your password from the login page: click Forgot Password "
    "and follow the email link.",
    "Offline mode lets you read and edit notes without internet; "
    "changes sync when you reconnect.",
]
SEARCH_VOCAB = build_vocab(FAQ)
FAQ_MATRIX = np.stack([embed(doc, SEARCH_VOCAB) for doc in FAQ])


def keyword_search(query, docs):
    return [doc for doc in docs if query.lower() in doc.lower()]


def search(query, k=3):
    scores = np.array([cosine_similarity(embed(query, SEARCH_VOCAB), row)
                       for row in FAQ_MATRIX])
    best = np.argsort(scores)[::-1][:k]
    return [(float(scores[i]), FAQ[i]) for i in best]


query = "how do i get my money back"
print("search Q1 -> keyword:", keyword_search(query, FAQ))
print("search Q1 -> semantic:", round(search(query, k=1)[0][0], 3),
      search(query, k=1)[0][1][:35] + "...")
# -> keyword: [] | semantic: 0.378 'Full refund within 30 days:...'

# Q2: Raw dot products ignore document LENGTH: a rambling doc that
#     happens to contain the 2 query words scores the same dot (2)
#     as a doc made of exactly those words. Cosine divides by the
#     norms, so the focused doc wins. (With count embeddings the
#     long-doc blow-up is even bigger.)
V2 = {"refund": 0, "money": 1, "cat": 2, "ship": 3, "note": 4}
q = embed("refund money", V2)
focused = embed("full refund money back", V2)
rambling = embed("refund money cat ship note", V2)
print("search Q2 -> raw dot:", np.dot(q, focused), np.dot(q, rambling),
      "| cosine:", round(cosine_similarity(q, focused), 3),
      round(cosine_similarity(q, rambling), 3))
# -> raw dot: 2.0 2.0 (tie!) | cosine: 1.0 0.632 (focused wins)

# Q3: Wrap search() and drop scores at or below the threshold, so
#     unrelated queries return [] instead of junk matches.


def only_relevant(query, threshold=0.05, k=3):
    return [(s, d) for s, d in search(query, k=k) if s > threshold]


print("search Q3 ->", len(only_relevant("how do i get my money back")),
      "relevant hit(s); unrelated:", only_relevant("teleporting dragons"))
# -> 1 relevant hit(s); unrelated: []
#     Beware stop words: "teleport my files to mars" is NOT empty
#     here -- its "to" matches the refund doc (score 0.267).

# Q4: All docs, no crash: argsort returns 7 (here 3) indices and
#     [:99] silently keeps every one of them -- numpy slices never
#     raise on over-long ranges (unlike indexing). search() returns
#     min(k, number of docs) results.
print("search Q4 ->", len(search("refund", k=99)), "results for k=99")
# -> 3 results for k=99


# ------------------------------------------------------------------
# simple_rag.py
# ------------------------------------------------------------------
# Q1: The GENERATE step does the picking: simulated_llm_answer
#     scores every retrieved sentence by shared question words and
#     returns the best. [1] is a CITATION: "this sentence came from
#     context doc 1", so the user can check the answer is grounded
#     in the FAQ rather than invented.

STOP = {"the", "a", "to", "of", "and", "is"}


def rag_tokenize(text):
    return [w for w in text.lower().replace("?", "").replace(".", "").split()
            if w not in STOP]


KB = [
    "Full refund within 30 days: your money goes back to the "
    "original payment method.",
    "Reset your password from the login page: click Forgot Password "
    "and follow the email link.",
    "Offline mode lets you read and edit notes without internet; "
    "changes sync when you reconnect.",
]
KB_VOCAB = build_vocab(KB)
KB_MATRIX = np.stack([embed(doc, KB_VOCAB) for doc in KB])


def rag_search(question, k=2):
    scores = np.array([cosine_similarity(embed(question, KB_VOCAB), row)
                       for row in KB_MATRIX])
    best = np.argsort(scores)[::-1][:k]
    return [(float(scores[i]), KB[i]) for i in best]


def fake_llm(question, contexts):
    q_words = set(rag_tokenize(question))
    best, best_score, tag = "I don't know - that is not in my documents.", 0, 0
    for n, ctx in enumerate(contexts, start=1):
        for sentence in ctx.split(". "):
            score = len(q_words & set(rag_tokenize(sentence)))
            if score > best_score:
                best, best_score, tag = sentence.strip(), score, n
    return f"{best} [{tag}]" if best_score else best


def rag_answer(question, k=2, min_score=0.0):
    contexts = [doc for score, doc in rag_search(question, k)
                if score > min_score]
    return fake_llm(question, contexts)


print("rag Q1 ->", rag_answer("How do I get my money back?"))
# -> Full refund within 30 days: your money goes back to the
#    original payment method. [1]

# Q2: With the filter gone, top-k stuffs the context with 0.000-
#     score docs. The prompt then presents unrelated text AS
#     context. Our stand-in still refuses (it only copies
#     sentences), but a real LLM generating freely will blend that
#     noise into a confident, wrong answer -- a hallucination.
#     Two guards: drop score <= 0 chunks AND keep "say you don't
#     know" in the system prompt.
leaked = [doc[:35] + "..." for _, doc in rag_search("Who is the CEO?")]
print("rag Q2 -> unfiltered context:", leaked)
print("rag Q2 -> stand-in answer:", rag_answer("Who is the CEO?"))
# -> context includes docs scoring 0.000; stand-in still says
#    "I don't know" -- a real LLM might not.

# Q3: The best score in this whole KB is 0.378 (the money-back
#     question). A 0.5 threshold drops EVERY doc for EVERY
#     question, so the bot always answers "I don't know" even when
#     the FAQ has the answer. Thresholds must be calibrated on the
#     real embedding model's score range, not guessed.
print("rag Q3 -> best score:", round(rag_search("How do I get my money "
      "back?", k=1)[0][0], 3), "so 0.5 filter gives:",
      rag_answer("How do I get my money back?", min_score=0.5))
# -> best score: 0.378 so 0.5 filter gives: I don't know - ...

# Q4: The SYSTEM prompt carries standing rules ("answer ONLY from
#     the context, cite, admit gaps") so they apply to every
#     request and are not buried in, or overridden by, user text;
#     the user message then stays pure DATA (numbered context +
#     question) that you can rebuild per question. Splitting roles
#     this way is also how chat APIs are designed, and some give
#     system content extra weight.
