"""
=====================================================================
TOPIC: RAG - Answering From Your Own Documents
=====================================================================

SCENARIO
--------
The NimbusNote support bot must answer questions using company FAQs
-- not its own imagination. Retrieval-Augmented Generation (RAG)
does this in three steps: RETRIEVE the few documents (chunks) that
match the question, AUGMENT the prompt by gluing them in, GENERATE
an answer that cites them. Grounded answers, fewer hallucinations,
and the bot stays correct even for facts the model never learned.

TOPIC
-----
- The prompt has two roles: SYSTEM sets the rules ("answer ONLY
  from the context, cite as [1], say you don't know otherwise");
  the USER message carries the numbered context plus the question.
- Below, the GENERATE step is a SIMULATED answerer: it picks the
  retrieved sentence sharing the most words with the question. It
  stands in for a real LLM API call -- the prompt built here is the
  real one you would send (see PRODUCTION in the code).
- Gotcha: if retrieval returns 0 relevant chunks, a real LLM will
  happily improvise. Filter zero scores AND keep the system line
  "say you don't know" -- defense in depth.
- CHUNKING: we embed one short FAQ per vector. Long docs must be
  split into overlapping chunks first (comment in the code).

QUESTIONS
---------
Q1. For "How do I get my money back?", which RAG step picks the
    exact sentence, and what does the [1] in the answer mean?
Q2. An off-topic question ("Who is the CEO?") scores 0 on every
    doc. If you delete the `if score > 0` filter, what does the
    prompt contain and what would a real LLM probably do?
Q3. Spot the bug: a teammate raises the filter to `score > 0.5`
    for "higher quality". What does the bot now answer for EVERY
    question, and why?
Q4. Why does "answer ONLY from the context" belong in the SYSTEM
    prompt rather than the user message?

Run: python 17_rag/simple_rag.py
Answers: answers/17_rag.py
=====================================================================
"""

import numpy as np

# Same toy embedder as embeddings.py, minus 6 stop words (words like
# "the" otherwise fake-match every document). PRODUCTION SWAP: the
# embed function becomes one embedding-model API call -- no key here.


def tokenize(text):
    stop = {"the", "a", "to", "of", "and", "is"}
    return [w for w in text.lower().replace("?", "").replace(".", "").split()
            if w not in stop]


def build_vocab(corpus):
    words = sorted({w for doc in corpus for w in tokenize(doc)})
    return {word: idx for idx, word in enumerate(words)}


def embed(text, vocab):
    vec = np.zeros(len(vocab))
    for word in tokenize(text):
        if word in vocab:
            vec[vocab[word]] = 1.0
    return vec


def cosine_similarity(a, b):
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    return 0.0 if denom == 0 else float(np.dot(a, b) / denom)


KNOWLEDGE_BASE = [
    "Full refund within 30 days: your money goes back to the "
    "original payment method.",
    "Reset your password from the login page: click Forgot Password "
    "and follow the email link.",
    "Offline mode lets you read and edit notes without internet; "
    "changes sync when you reconnect.",
    "The Pro plan costs 9 dollars per month. The free plan includes "
    "100 notes on 1 device.",
    "Standard delivery takes 3 to 5 business days. We ship to 40 "
    "countries.",
]

VOCAB = build_vocab(KNOWLEDGE_BASE)
KB_MATRIX = np.stack([embed(doc, VOCAB) for doc in KNOWLEDGE_BASE])

# CHUNKING (concept): one short FAQ per vector keeps each vector on
# one topic. A 50-page PDF embedded whole blends every topic into a
# blurry vector -- so split it into overlapping chunks (e.g. 500
# tokens with 100 overlap, so no idea is cut at a boundary), embed
# EACH chunk, and retrieve the few chunks that answer the question.


def search(question, k=2):
    scores = np.array([cosine_similarity(embed(question, VOCAB), row)
                       for row in KB_MATRIX])
    best = np.argsort(scores)[::-1][:k]
    return [(float(scores[i]), KNOWLEDGE_BASE[i]) for i in best]


SYSTEM_PROMPT = (
    "You are the NimbusNote support assistant. Answer ONLY from the "
    "numbered context. If the answer is not there, say you don't "
    "know. Cite sources as [1], [2]."
)


def build_user_prompt(question, contexts):
    numbered = "\n".join(f"[{i + 1}] {c}" for i, c in enumerate(contexts))
    return f"Context:\n{numbered}\n\nQuestion: {question}"


def simulated_llm_answer(question, contexts):
    """STAND-IN for a real LLM call: returns the retrieved sentence
    sharing the most words with the question, with its [n] tag."""
    q_words = set(tokenize(question))
    best, best_score, best_tag = "I don't know.", 0, 0
    for tag, ctx in enumerate(contexts, start=1):
        for sentence in ctx.split(". "):
            score = len(q_words & set(tokenize(sentence)))
            if score > best_score:
                best, best_score, best_tag = sentence.strip(), score, tag
    if best_score == 0:  # nothing in context relates to the question
        return "I don't know - that is not in my documents."
    return f"{best} [{best_tag}]"


def rag_answer(question, k=2):
    # 1 RETRIEVE: keep only docs with a real (positive) match.
    contexts = [doc for score, doc in search(question, k) if score > 0]
    # 2 AUGMENT: system rules + numbered context + question.
    print(f"--- prompt sent (system: {SYSTEM_PROMPT[:40]}...) ---")
    print(build_user_prompt(question, contexts))
    # 3 GENERATE. PRODUCTION: one API call with this exact prompt:
    #   client.messages.create(model=..., system=SYSTEM_PROMPT,
    #       messages=[{"role": "user",
    #                  "content": build_user_prompt(question, contexts)}])
    return simulated_llm_answer(question, contexts)


print("Q:", "How do I get my money back?")
print("A:", rag_answer("How do I get my money back?"))
print()
print("Q: Who is the CEO?")
print("A:", rag_answer("Who is the CEO?"))


# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/17_rag.py
# ------------------------------------------------------------------
# Q1: Which step picks the sentence, and what does [1] cite?
# Q2: What leaks into the prompt with no score filter?
# Q3: What does a 0.5 threshold do to every answer here?
# Q4: SYSTEM prompt vs user message -- why?
