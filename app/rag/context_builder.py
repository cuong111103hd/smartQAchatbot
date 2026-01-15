from typing import List, Dict

def build_context(retrieved_docs: List[Dict], max_chars: int = 3000)-> str:
    context = ""
    total_chars = 0

    for doc in retrieved_docs:
        snippet = (
            f"[Section: {doc['metadata']['section']}] | "
            f"Page: {doc['metadata']['page']}]\n"
            f"{doc['text']}\n\n"
        )

        if total_chars + len(snippet) > max_chars:
            break

        context += snippet
        total_chars += len(snippet)

    return context.strip()