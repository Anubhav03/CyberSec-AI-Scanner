from agents.base_agent_settings import create_agent
import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["CREWAI_ALLOW_LOCAL_MODE"] = "true"
os.environ["CREWAI_STORAGE_BACKEND"] = "memory"   # ⬅ key fix


judge_agent = create_agent(
    role="Risk Assessment Judge",
    goal="Score risks based on realistic severity, likelihood, and impact word limit 150.",
    backstory=(
        "You evaluate cybersecurity risks using frameworks like CVSS, OWASP, and likelihood modelling. "
        "You assign severity labels (Low/Medium/High/Critical) and select top priority actions."
    ),
)
