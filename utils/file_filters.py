from pathlib import Path
from utils.constants import ALLOWED_EXT, IGNORE_DIRS


def should_scan(file_path: Path) -> bool:
    """Return True if a file should be scanned based on extension and directory."""
    
    if any(dir_name in str(file_path).lower() for dir_name in IGNORE_DIRS):
        return False

    if file_path.suffix.lower() in ALLOWED_EXT:
        return True

    if file_path.name.lower() in ("dockerfile", "docker-compose.yml", "package.json"):
        return True

    return False
