"""
Solution for Project 08 - Semantic FAQ Search + RAG Answer.

Run it with:
    python answers/projects/project_08_semantic_faq_solution.py

Builds a toy bag-of-words embedding (numpy) over 8 FAQ articles about
the fictional NimbusNote app, ranks documents against a query with
cosine similarity, prints the prompt that WOULD go to a real LLM, and
composes clearly-labeled simulated answers. 100% offline and keyless:
the LLM call exists only as a commented-out real shape.
"""

from __future__ import annotations

import re
from textwrap import indent

import numpy as np

FAQ_DOCS: list[dict[str, str]] = [
    {"id": "faq_offline", "title": "Offline access",
     "text": "NimbusNote works fully offline. Notes you open are cached on "
             "your device and sync automatically the next time you connect."},
    {"id": "faq_pricing", "title": "Pricing",
     "text": "The free plan includes 3 notebooks and 1000 notes. The Pro plan "
             "costs 5 dollars per month and unlocks unlimited notebooks and "
             "version history."},
    {"id": "faq_sharing", "title": "Sharing and collaboration",
     "text": "Share any notebook by entering a teammate's email. People with "
             "a read only link can view your notes but never edit them."},
    {"id": "faq_export", "title": "Export and backup",
     "text": "Export everything at once from Settings, then choose Markdown, "
             "PDF or HTML. Backups download as a single zip file."},
    {"id": "faq_security", "title": "Security",
     "text": "All notes are encrypted with AES 256 both in transit and at "
             "rest. Two factor authentication is available on every plan."},
    {"id": "faq_mobile", "title": "Mobile apps",
     "text": "NimbusNote has apps for iOS and Android. Scans of handwritten "
             "pages become searchable text through on device OCR."},
    {"id": "faq_search", "title": "Search",
     "text": "Search covers every notebook and quotes give exact phrase "
             "matches. Search also looks inside attached PDF files."},
    {"id": "faq_refund", "title": "Cancellation and refunds",
     "text": "You can cancel your subscription any time from Settings. "
             "Yearly plans come with a 30 day money back guarantee, no "
             "questions asked."},
]

DEMO_QUERIES = [
    "Can I use NimbusNote offline on a plane?",
    "How much does the paid plan cost?",
    "Is my data encrypted, and can I get my money back?",
]


def tokenize(text: str) -> list[str]:
    """Task 1: lowercase words and numbers only -- no punctuation."""
    return re.findall(r"[a-z0-9]+", text.lower())


def build_vectorizer(docs: list[dict[str, str]]) -> tuple[dict[str, int], np.ndarray]:
    """Task 2: the vocabulary + one count row per document.

    Sorted set -> deterministic column order, so the vocab (and the
    vectors) come out identical on every machine.
    """
    words = sorted({token for doc in docs for token in tokenize(doc["text"])})
    vocab = {word: column for column, word in enumerate(words)}
    matrix = np.zeros((len(docs), len(vocab)), dtype=float)
    for row, doc in enumerate(docs):
        for token in tokenize(doc["text"]):
            matrix[row, vocab[token]] += 1.0
    return vocab, matrix


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Task 3: the angle between two vectors, as a -1..1 score.

    Zero-norm guard first: an all-zero vector (no overlap at all)
    would otherwise divide by 0.0.
    """
    denominator = np.linalg.norm(a) * np.linalg.norm(b)
    if denominator == 0.0:
        return 0.0
    return float(np.dot(a, b) / denominator)


def vectorize_query(query: str, vocab: dict[str, int]) -> np.ndarray:
    """Task 4: the query in the SAME vector space as the documents.

    Words outside the vocabulary are ignored -- a toy embedding's
    biggest weakness (real embeddings generalize to unseen words).
    """
    vector = np.zeros(len(vocab), dtype=float)
    for token in tokenize(query):
        if token in vocab:
            vector[vocab[token]] += 1.0
    return vector


def search(query: str, docs: list[dict], vocab: dict[str, int],
           matrix: np.ndarray, k: int = 2) -> list[tuple[float, dict]]:
    """Task 5: score every doc, sort best first, keep the top k."""
    query_vec = vectorize_query(query, vocab)
    scored = [(cosine_similarity(query_vec, matrix[row]), doc)
              for row, doc in enumerate(docs)]
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return scored[:k]


def build_prompt(query: str, results: list[tuple[float, dict]]) -> str:
    """Task 6: the exact string a real LLM would receive.

    Everything the model will "know" about NimbusNote lives in here.
    Instructions first, then numbered context, then the question.
    """
    blocks = [f"[{position}] ({doc['id']}) {doc['text']}"
              for position, (_, doc) in enumerate(results, start=1)]
    context = "\n".join(blocks) if blocks else "(nothing retrieved)"
    return (
        "You are the NimbusNote support assistant.\n"
        "Answer the user's question using ONLY the context below.\n"
        "If the context does not answer it, say you will escalate "
        "to a human colleague.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}\n"
        "Answer:"
    )


def compose_answer(query: str, results: list[tuple[float, dict]]) -> str:
    """Task 7: the SIMULATED LLM -- this body is what the real call replaces.

    The real thing (module 16) is exactly this, no more:

        import anthropic          # pip install anthropic -- needs a key
        client = anthropic.Anthropic()
        response = client.messages.create(
            model="claude-opus-5-5",
            max_tokens=1024,
            system="You are the NimbusNote support assistant. Answer using "
                   "only the provided context; if it is not enough, say so.",
            messages=[{"role": "user",
                       "content": build_prompt(query, results)}],
        )
        return next(b.text for b in response.content if b.type == "text")

    The simulated version: best doc's title + first sentence, plus the
    runner-up as related reading. Zero-score retrieval gets a refusal.
    """
    if not results or results[0][0] == 0.0:
        return ("[SIMULATED LLM] I could not find a matching FAQ article -- "
                "escalating this to a human colleague.")
    best_score, best_doc = results[0]
    first_sentence = best_doc["text"].split(". ")[0].rstrip(".") + "."
    lines = [f"[SIMULATED LLM] From the '{best_doc['title']}' article:",
             f"  {first_sentence}"]
    if len(results) > 1 and results[1][0] > 0.0:
        lines.append(f"  Related reading: '{results[1][1]['title']}'.")
    return "\n".join(lines)


def main() -> None:
    print("SEMANTIC FAQ SEARCH + RAG ANSWER -- solution")

    vocab, matrix = build_vectorizer(FAQ_DOCS)
    print(f"  knowledge base: {len(FAQ_DOCS)} docs, "
          f"{len(vocab)} unique words -> matrix {matrix.shape}")

    for number, query in enumerate(DEMO_QUERIES, start=1):
        print(f"\n{'=' * 58}\nQuery {number}: {query}\n{'=' * 58}")
        results = search(query, FAQ_DOCS, vocab, matrix, k=2)
        print("\nRetrieved (cosine similarity):")
        for score, doc in results:
            print(f"  {score:.3f}  {doc['id']:<14} ({doc['title']})")
        if number == 1:
            print("\nThe prompt that would go to the real LLM:")
            print(indent(build_prompt(query, results), "  | "))
        print("\n" + compose_answer(query, results).replace("\n", "\n"))

    print("\nLast query retrieved security AND refund docs from one question")
    print("-- that only works because the question and the docs share words.")
    print("Swap the toy vectors for real embeddings later: same pipeline.")


if __name__ == "__main__":
    main()
