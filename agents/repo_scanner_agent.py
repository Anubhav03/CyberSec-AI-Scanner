from agents.base_agent_settings import create_agent
import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["CREWAI_ALLOW_LOCAL_MODE"] = "true"
os.environ["CREWAI_STORAGE_BACKEND"] = "memory"   # ⬅ key fix


repo_scanner_agent = create_agent(
    role="Repository Scanner",
    goal="Analyze a codebase for security vulnerabilities, misconfigurations, and sensitive data exposure.",
    backstory=(
        "You are an experienced cybersecurity auditor specialized in static analysis. "
        "You scan code repositories for high-risk patterns such as tokens, exposed credentials, "
        "weak cryptography, and misconfigured permissions."
    )
)
