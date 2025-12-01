# Allowed code & config file types
ALLOWED_EXT = [
    ".py", ".js", ".ts", ".java", ".go", ".rb", ".php", ".rs",
    ".json", ".yml", ".yaml", ".env", ".toml", ".ini", ".gradle"
]

# Ignore directories during scanning
IGNORE_DIRS = [
    "node_modules", "dist", "build", ".git", "__pycache__", "venv", "coverage", "logs"
]

# Model used across the project (fallback)
DEFAULT_MODEL = "gpt-4.1-mini"

# Report formats supported
SUPPORTED_REPORTS = ["md", "html", "pdf"]
