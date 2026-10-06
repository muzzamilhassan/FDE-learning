"""
=====================================================================
PROJECT: Semantic FAQ Search + RAG Answer  (Difficulty: advanced)
=====================================================================

SCENARIO
--------
NimbusNote is a fictional note-taking app whose support inbox drowns
in the same eight questions. You will build a tiny "ask the docs"
feature: embed the FAQ articles as vectors, rank them against a user
question with cosine similarity, and hand the best matches to an
answer builder. There is no API key here -- the embedding and the
LLM are both simulated -- but every seam where the real thing plugs
in is clearly labeled.

WHAT YOU WILL PRACTICE
----------------------
- Text -> vectors: bag-of-words counts with numpy (from module 13)
- Cosine similarity: dot products and norms (from module 13)
- Top-k retrieval: the "R" in RAG (from module 17)
- Building an LLM prompt with retrieved context (from module 17)
- Where the real LLM call goes -- real prompt shape in comments (module 16)
- dicts, sets, sorting with key= (modules 02/04)

YOUR TASKS
----------
1. tokenize(text): lowercase and keep runs of [a-z0-9]. So
   "Prices? PRO $5!" -> ["prices", "pro", "5"].
2. build_vectorizer(docs): build the vocab {word: column index} and
   a count matrix with one row per document. Return (vocab, matrix).
3. cosine_similarity(a, b): dot(a, b) / (||a|| * ||b||). Return 0.0
   when either vector is all zeros -- or you divide by zero.
4. vectorize_query(query, vocab): turn a question into a vector that
   lines up with the matrix columns (ignore unknown words).
5. search(query, docs, vocab, matrix, k=2): score every doc, sort
   best first, return the top k as (score, doc) pairs.
6. build_prompt(query, results): assemble the EXACT prompt you would
   send to a real LLM: instructions + numbered context + question.
7. compose_answer(query, results): the SIMULATED LLM. Compose a short
   answer from the retrieved docs -- its docstring shows the real
   API call that would replace it.
8. main(): run 3 demo queries end to end: retrieval scores, the built
   prompt (printed once), and the final answers.

STARTER CODE
------------
Complete the TODOs below. Run with:
    python 99_projects/project_08_semantic_faq.py

100% offline and keyless. Hints are inline.
A full solution is in answers/projects/.
=====================================================================
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


# ------------------------------------------------------------------
# TODOs -- everything below is yours
# ------------------------------------------------------------------

def tokenize(text: str) -> list[str]:
    """TODO 1: lowercase the text and keep runs of [a-z0-9].

    Hint: return re.findall(r"[a-z0-9]+", text.lower())
    """
    print("TODO: implement tokenize()")
    return []


def build_vectorizer(docs: list[dict[str, str]]) -> tuple[dict[str, int], np.ndarray]:
    """TODO 2: the vocabulary + a count matrix.

    1. collect every token from every doc into ONE sorted set
    2. vocab = {word: column_index} from that set
    3. matrix = np.zeros((len(docs), len(vocab))); then for each doc
       row, for each of its tokens: matrix[row, vocab[token]] += 1
    Return (vocab, matrix).
    """
    print("TODO: implement build_vectorizer()")
    return {}, np.zeros((0, 0))


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """TODO 3: float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))).

    Guard clause first: if either norm is 0.0, return 0.0.
    """
    print("TODO: implement cosine_similarity()")
    return 0.0


def vectorize_query(query: str, vocab: dict[str, int]) -> np.ndarray:
    """TODO 4: a zeros vector of len(vocab); +1 in vocab[token] for each
    query token that IS in the vocab. Unknown words are simply ignored."""
    print("TODO: implement vectorize_query()")
    return np.zeros(len(vocab))


def search(query: str, docs: list[dict], vocab: dict[str, int],
           matrix: np.ndarray, k: int = 2) -> list[tuple[float, dict]]:
    """TODO 5: vectorize the query, then score EVERY doc with
    cosine_similarity(query_vec, matrix[row]).

    Collect (score, doc) pairs, sort by score descending, slice [:k].
    """
    print("TODO: implement search()")
    return []


def build_prompt(query: str, results: list[tuple[float, dict]]) -> str:
    """TODO 6: return ONE string that a real LLM would receive.

    Suggested layout (order matters -- instructions, context, question):
        You are the NimbusNote support assistant.
        Answer using ONLY the context below. If it does not contain
        the answer, say you will escalate to a human.
        Context:
        [1] (faq_pricing) The free plan includes...
        [2] (faq_security) All notes are encrypted...
        Question: <the user's question>
        Answer:

    Whatever an LLM knows, it knows from THIS string. Make it good.
    """
    print("TODO: implement build_prompt()")
    return ""


def compose_answer(query: str, results: list[tuple[float, dict]]) -> str:
    """TODO 7: the SIMULATED LLM -- clearly labeled as simulated.

    IN REAL LIFE (module 16), this whole body is one API call that
    receives the prompt from build_prompt() and returns text:

        import anthropic            # pip install anthropic -- needs a key
        client = anthropic.Anthropic()
        response = client.messages.create(
            model="claude-opus-5-5",
            max_tokens=1024,
            system="You are the NimbusNote support assistant.",
            messages=[{"role": "user",
                       "content": build_prompt(query, results)}],
        )
        return next(b.text for b in response.content if b.type == "text")

    The simulated version: compose a short answer from the top doc
    (title + its first sentence) and point at the second doc as
    related reading. Prefix it with "[SIMULATED LLM]".
    """
    print("TODO: implement compose_answer()")
    return ""


def main() -> None:
    print("=" * 58)
    print("  SEMANTIC FAQ SEARCH + RAG ANSWER -- starter")
    print("  Retrieve the right docs, then answer from them.")
    print("=" * 58)

    vocab, matrix = build_vectorizer(FAQ_DOCS)
    if matrix.size == 0:
        print("\n  The knowledge base is not embedded yet --")
        print("  implement tasks 1-5 to bring the search to life.")
        return

    for number, query in enumerate(DEMO_QUERIES, start=1):
        print(f"\nQuery {number}: {query}")
        results = search(query, FAQ_DOCS, vocab, matrix, k=2)
        for score, doc in results:
            print(f"  {score:.3f}  {doc['id']}  ({doc['title']})")
        if number == 1:
            print("\n  --- the prompt that would go to the real LLM ---")
            print(indent(build_prompt(query, results), "  "))
        print("\n  " + compose_answer(query, results).replace("\n", "\n  "))

    print("\nThat is RAG: retrieve first, answer only from what you retrieved.")


if __name__ == "__main__":
    main()
