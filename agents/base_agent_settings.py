import os
from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ Missing GROQ_API_KEY in your .env file")


# 🔹 Groq LLM configuration
groq_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=GROQ_API_KEY,
    temperature=0.2,
    max_tokens=200  # Hard safety limit (≈150 words)
)


def enforce_word_limit(text: str, limit: int = 150) -> str:
    """Trim response to N words as a second safety layer."""
    words = text.split()
    return " ".join(words[:limit]) + ("..." if len(words) > limit else "")


def create_agent(role, goal, backstory):
    return Agent(
        role=role,
        goal=f"{goal}\n\n📌 Output Rules:\n- Response MUST NOT exceed 150 words.\n- Use concise bullet points when possible.\n- Avoid unnecessary explanations.\n",
        backstory=backstory,
        llm=groq_llm,
        verbose=True,
        response_format="text",
        max_retry_attempts=2,
        postprocess=enforce_word_limit  # <- final enforced word-trim safeguard
    )
