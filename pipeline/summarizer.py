from langchain_groq import ChatGroq

# Fix import path shift in latest LangChain
from langchain_core.messages import HumanMessage, SystemMessage


SYSTEM_PROMPT = """
You are the System Architecture Summary Agent.

Analyze the following repository metadata and create a clean cybersecurity relevant summary.

Output format:

System Description:
Tech Stack:
Authentication Model:
Data Sensitivity Level:
Hosting / Deployment:
Security Controls Found:
Potential Weakness Indicators:
"""


def generate_system_summary(metadata_text: str) -> str:
    """Summarizes extracted repo structure using Groq LLM."""

    llm = ChatGroq(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        temperature=0.2
    )

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"Repository Metadata:\n{metadata_text}")
    ]

    response = llm.invoke(messages)

    # Normalize all possible return types into a clean string
    if hasattr(response, "content"):
        return str(response.content).strip()

    if isinstance(response, list):
        return "\n".join(str(item) for item in response).strip()

    return str(response).strip()
