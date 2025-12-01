import hashlib
from typing import Dict


def hash_content(content: str) -> str:
    """Generate a lightweight SHA1 hash for caching or diff detection."""
    return hashlib.sha1(content.encode("utf-8")).hexdigest()


def extract_dependency_signals(files: Dict) -> str:
    """Lightweight heuristic extractor for tech stack classification."""
    signals = []

    for f in files:
        name = f["filename"].lower()
        content = f["content"]

        if "package.json" in name:
            signals.append("Detected Node.js dependencies")
        if "requirements.txt" in name:
            signals.append("Python dependency file found")
        if "dockerfile" in name:
            signals.append("Docker deployment detected")
        if "auth" in content.lower() or "jwt" in content.lower():
            signals.append("Possible authentication logic detected")

    return "\n".join(signals) or "No obvious indicators found."
