"""
=====================================================================
TOPIC: Semantic Search - Rank Documents by Meaning-ish Distance
=====================================================================

SCENARIO
--------
A support bot for the fictional note app "NimbusNote" has 7 FAQ
documents. A user types "how do I get my money back". Exact-phrase
keyword search returns nothing -- no FAQ contains that sentence.
Semantic search embeds the question and every FAQ, then returns the
docs whose vectors point the same way: the refund policy, even
though it never says those words.

TOPIC
-----
- Pipeline: embed ALL docs once (a 2-D numpy matrix, one row per
  doc) -> embed the query -> cosine similarity of the query against
  every row -> sort, keep top-k. Embedding docs is done once;
  only the query is embedded per search.
- Keyword search (substring / word-in-doc) is brittle: it needs the
  exact wording. Vector search needs only SHARED words -- and a
  real embedding model needs only shared MEANING.
- np.argsort(scores)[::-1][:k] gives the k best doc indices.
- Gotcha: raw dot products (matrix @ query) grow with document
  length, so long docs always win. Cosine normalizes this away.
- Honest limit: our toy still matches WORDS. "cash returned" finds
  nothing here; only a trained embedding model closes that gap.

QUESTIONS
---------
Q1. Why does keyword_search find nothing for the money-back query
    while search() ranks the refund doc first?
Q2. Spot the bug: scores = doc_matrix @ q_vec, then top-k. The team
    notices long FAQs always rank first. What is wrong, and what
    is the one-line fix?
Q3. Write only_relevant(query, threshold) that uses search() but
    drops results scoring at or below threshold, so unrelated
    queries return an empty list.
Q4. What does search(query, k=99) return for 7 docs -- crash, k
    docs, or 7 docs? Check, then explain why.

Run: python 17_rag/semantic_search.py
Answers: answers/17_rag.py
=====================================================================
"""

import numpy as np

# ------------------------------------------------------------------
# TOPIC EXAMPLES: a tiny FAQ knowledge base, embedded and ranked
# ------------------------------------------------------------------


def tokenize(text):
    return text.lower().replace("?", "").replace(".", "").split()


def build_vocab(corpus):
    words = sorted({w for doc in corpus for w in tokenize(doc)})
    return {word: idx for idx, word in enumerate(words)}


def embed(text, vocab):
    # Toy embedder. PRODUCTION SWAP: one embedding-model API call
    # returning a dense vector per text; no API key needed here.
    vec = np.zeros(len(vocab))
    for word in tokenize(text):
        if word in vocab:
            vec[vocab[word]] = 1.0
    return vec


def cosine_similarity(a, b):
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom == 0:
        return 0.0
    return float(np.dot(a, b) / denom)


FAQ_DOCS = [
    "Full refund within 30 days: your money goes back to the "
    "original payment method.",
    "We ship to 40 countries. Standard delivery takes 3 to 5 "
    "business days.",
    "Reset your password from the login page: click Forgot Password "
    "and follow the email link.",
    "Offline mode lets you read and edit notes without internet; "
    "changes sync when you reconnect.",
    "The Pro plan costs 9 dollars per month. The free plan includes "
    "100 notes on 1 device.",
    "Delete your account in Settings. All notes are removed "
    "permanently after 30 days.",
    "Nimbus connects to Slack, Google Drive and GitHub on every "
    "plan.",
]

VOCAB = build_vocab(FAQ_DOCS)
# One row per doc, embedded ONCE at startup -- queries reuse this.
DOC_MATRIX = np.stack([embed(doc, VOCAB) for doc in FAQ_DOCS])
print("doc matrix:", DOC_MATRIX.shape, "(docs x vocabulary slots)")


def keyword_search(query, docs):
    """Exact-phrase match: the WHOLE query must appear verbatim."""
    return [doc for doc in docs if query.lower() in doc.lower()]


def search(query, k=2):
    """Embed the query, score vs every doc, return top-k as
    (score, doc) tuples, best first."""
    q_vec = embed(query, VOCAB)
    scores = np.array([cosine_similarity(q_vec, row) for row in DOC_MATRIX])
    best = np.argsort(scores)[::-1][:k]
    return [(float(scores[i]), FAQ_DOCS[i]) for i in best]


query = "how do i get my money back"
print("keyword_search hits:", keyword_search(query, FAQ_DOCS))
print("semantic search top 2:")
for score, doc in search(query, k=2):
    print(f"  {score:.3f}  {doc[:60]}...")
# Same query, opposite outcomes: substring needs exact wording,
# vector search needs shared words ("money", "back").

for score, doc in search("reset my password", k=1):
    print(f"straight hit: {score:.3f}  {doc[:60]}...")


# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/17_rag.py
# ------------------------------------------------------------------
# Q1: keyword vs semantic matching strategies -- why the difference?
# Q2: Why do long docs win with raw dot products?
# Q3: Write only_relevant(query, threshold).
# Q4: search("...", k=99) on 7 docs returns what?
