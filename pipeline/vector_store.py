import os
import cohere
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import Chroma

VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "/tmp/chroma")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

def build_vector_store(chunks):
    if not chunks:
        print("⚠️ No chunks found — skipping vector DB build.")
        return None

    print("📦 Building embeddings using Cohere (v3)...")

    # Create Cohere client
    client = cohere.Client(api_key=COHERE_API_KEY)

    embeddings = CohereEmbeddings(
        client=client,
        async_client=None,   # <-- fixes the missing argument
        model="embed-english-light-v3.0"
    )

    vectordb = Chroma.from_texts(
        texts=[chunk["text"] for chunk in chunks],
        metadatas=[
            {"filename": chunk["filename"], "path": chunk["source_path"]}
            for chunk in chunks
        ],
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    vectordb.persist()
    print("✅ Vector DB saved successfully.")

    return vectordb
