from typing import List
from langchain_community.vectorstores import Chroma


def retrieve_relevant_code(query: str, vectordb: Chroma, top_k: int = 5) -> str:
    """Searches vector DB for code or config relevant to the prompt."""
    results = vectordb.similarity_search(query, k=top_k)

    formatted = []
    for r in results:
        formatted.append(
            f"🔥 MATCH FROM: {r.metadata['file']}\n"
            f"📄 PATH: {r.metadata['path']}\n\n"
            f"{r.page_content}\n"
            "─" * 50
        )

    return "\n\n".join(formatted)
