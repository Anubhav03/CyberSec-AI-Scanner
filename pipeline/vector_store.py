from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

import os

VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./embeddings/chroma")


def build_vector_store(chunks):
    """Build a vector DB using SentenceTransformer instead of Nomic."""
    
    if len(chunks) == 0:
        print("⚠️ No chunks found — skipping vector DB build.")
        return None

    print("📦 Building embeddings using SentenceTransformer...")

    embedder = SentenceTransformerEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectordb = Chroma.from_texts(
        texts=[chunk["text"] for chunk in chunks],
        metadatas=[{
            "filename": chunk["filename"],
            "path": chunk["source_path"]
        } for chunk in chunks],
        embedding=embedder,
        persist_directory=VECTOR_DB_PATH
    )

    vectordb.persist()
    print("✅ Vector database saved successfully.")

    return vectordb
