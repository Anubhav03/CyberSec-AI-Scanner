import os
from pathlib import Path
from typing import Union, List, Dict
from utils.constants import ALLOWED_EXT, IGNORE_DIRS


def scan_repository(repo_path: Union[str, Path]) -> List[Dict]:
    """Scans a project directory and extracts readable and relevant source files."""

    repo_path = Path(repo_path)
    collected_files: List[Dict] = []

    for root, dirs, files in os.walk(repo_path):
        # Remove ignored directories from traversal
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            file_path = Path(root) / file
            ext = file_path.suffix.lower()

            # Check if file should be scanned
            if ext in ALLOWED_EXT or file.lower() in ("dockerfile", "docker-compose.yml", "package.json"):
                try:
                    collected_files.append({
                        "filename": file,
                        "relative_path": str(file_path.relative_to(repo_path)),
                        "content": file_path.read_text(encoding="utf-8", errors="ignore")
                    })
                except Exception:
                    # Skip unreadable files safely
                    continue

    return collected_files
