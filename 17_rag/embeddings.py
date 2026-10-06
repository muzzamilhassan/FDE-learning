"""
=====================================================================
TOPIC: Embeddings - Turning Text Into Vectors
=====================================================================

SCENARIO
--------
You are building an AI app that answers questions over company
documents. A user asks "how do I get my money back", but no
document contains that exact phrase. Embeddings fix this: every
piece of text becomes a vector of numbers, and vectors that point
the same way are texts that belong together -- no exact wording
required. This is the foundation of semantic search and RAG.

TOPIC
-----
- An EMBEDDING maps text -> a fixed-length numeric vector.
  Similar texts end up as nearby vectors; you compare vectors, not
  strings.
- Here we build a TOY embedding from scratch: one vocabulary slot
  per unique word in the corpus, and a text's vector marks its
  words with a 1 (binary bag-of-words). Pure numpy, offline.
- Cosine similarity measures "nearby": dot(a, b) / (|a| * |b|).
  1.0 = same direction, 0.0 = nothing shared. The norms in the
  divisor stop long texts from winning just by being long.
- Gotcha: a text with no known words is the ZERO vector, and
  dividing by its norm (0) gives nan -- guard it.
- Bigger gotcha: toy vectors match WORDS, not meaning. "puppy" and
  "dog" share no slot and score 0.0. That gap is exactly why real
  apps use trained embedding models (see PRODUCTION below).

QUESTIONS
---------
Q1. Predict: cosine_similarity(v, v) for any nonzero vector v, and
    the score for two vectors that share no words.
Q2. Spot the bug: a teammate deletes the `if denom == 0` guard and
    embeds an all-unknown sentence. What does the function return
    (or raise), and why?
Q3. Write embed_counts(text, vocab) that counts words instead of
    using 0/1. Does the dog-vs-mouse similarity change? Try
    cosine_similarity(embed_counts("dog dog cat"), ...) to see when
    counts matter.

Run: python 17_rag/embeddings.py
Answers: answers/17_rag.py
=====================================================================
"""

import numpy as np

# ------------------------------------------------------------------
# TOPIC EXAMPLES: vocabulary -> binary vectors -> cosine similarity
# ------------------------------------------------------------------


def tokenize(text):
    """Toy preprocessing: lowercase, drop . and ?, split on spaces."""
    return text.lower().replace("?", "").replace(".", "").split()


def build_vocab(corpus):
    """One slot per unique word across all docs (sorted = stable)."""
    words = sorted({w for doc in corpus for w in tokenize(doc)})
    return {word: idx for idx, word in enumerate(words)}


def embed(text, vocab):
    """Text -> binary vector: 1.0 in the slot of each word present.

    PRODUCTION SWAP: a real app replaces THIS function with one
    embedding-model API call (Voyage / OpenAI / local model) that
    returns a dense vector per text. Everything downstream -- the
    cosine math, the ranking -- stays exactly the same:
        vectors = client.embeddings.create(model=..., input=texts)
    This file makes NO network calls and needs NO API key.
    """
    vec = np.zeros(len(vocab))
    for word in tokenize(text):
        if word in vocab:  # unseen words are skipped, not an error
            vec[vocab[word]] = 1.0
    return vec


def cosine_similarity(a, b):
    """dot / (|a| * |b|): 1.0 same direction, 0.0 unrelated."""
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom == 0:  # all-unseen text -> zero vector -> avoid nan
        return 0.0
    return float(np.dot(a, b) / denom)


corpus = [
    "the dog chases the cat",
    "the cat chases the mouse",
    "the quarterly revenue report grew",
]
vocab = build_vocab(corpus)
print("vocabulary slots:", list(vocab))

animals = embed("the dog chases the cat", vocab)
chase_2 = embed("the cat chases the mouse", vocab)
finance = embed("the quarterly revenue report grew", vocab)

print("animals vs other animals:", round(cosine_similarity(animals, chase_2), 3))
print("animals vs finance      :", round(cosine_similarity(animals, finance), 3))
# 0.75 vs 0.224: the animal sentences share 3 of their 4 filled
# slots, finance shares only "the". Nearby vectors = related
# topics, even for a toy.

# GOTCHA: toys match words, not meaning. "puppy" and "kitten" are
# not in the vocabulary, so this very similar sentence is the zero
# vector and scores 0.0 -- a trained model would score it HIGH.
puppy = embed("a puppy runs after a kitten", vocab)
print("puppy sentence vs animals:", cosine_similarity(puppy, animals))


# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/17_rag.py
# ------------------------------------------------------------------
# Q1: Predict the two values (identical vectors / zero shared words).
# Q2: What happens with no zero-vector guard?
# Q3: Write embed_counts(text, vocab) and test it on
#     "dog dog cat" vs "dog cat".
