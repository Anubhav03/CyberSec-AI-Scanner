from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List, Dict


def chunk_files(files: List[Dict], chunk_size: int = 2000, overlap: int = 200) -> List[Dict]:
    """Split code and config files into retrieval-friendly chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separators=["\nclass ", "\ndef ", "\n#", "\n", " ", ""]
    )

    chunks = []

    for file in files:
        split_chunks = splitter.split_text(file["content"])
        for chunk in split_chunks:
            chunks.append({
                "filename": file["filename"],
                "source_path": file["relative_path"],
                "text": chunk
            })

    print(f"✂️ Total chunks created: {len(chunks)}")
    return chunks
