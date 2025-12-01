import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

TOKEN_URL = "https://github.com/login/oauth/access_token"
USER_URL = "https://api.github.com/user"


def get_github_access_token(code: str):
    """Exchange auth code for access token."""
    response = requests.post(
        TOKEN_URL,
        headers={"Accept": "application/json"},
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code
        }
    )

    return response.json()


def get_github_user(token: str):
    """Fetch user profile using token."""
    response = requests.get(
        USER_URL,
        headers={"Authorization": f"Bearer {token}"}
    )
    return response.json()


def get_github_login_url():
    """Return GitHub login authorization URL."""
    if not CLIENT_ID:
        raise ValueError("❌ Missing GITHUB_CLIENT_ID in .env")

    return f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&scope=repo"


if __name__ == "__main__":
    print("⚠ Running standalone for testing only.")
