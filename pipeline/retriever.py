from typing import List
from langchain_community.vectorstores import Chroma

def retrieve_relevant_code(query: str, vectordb: Chroma, top_k: int = 5) -> str:
    """Search the vector DB using Cohere embeddings and return formatted matches."""
    
    results = vectordb.similarity_search(query, k=top_k)

    if not results:
        return "⚠️ No relevant code found for this query."

    formatted_results = []

    for r in results:
        filename = r.metadata.get("filename", "Unknown File")
        path = r.metadata.get("path", "Unknown Path")

        formatted_results.append(
            f"🔥 **MATCH SOURCE:** {filename}\n"
            f"📁 **Path:** {path}\n\n"
            f"```\n{r.page_content}\n```\n"
            + ("─" * 50)
        )

    return "\n\n".join(formatted_results)
