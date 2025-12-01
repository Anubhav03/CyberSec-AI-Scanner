from agents.base_agent_settings import create_agent

judge_agent = create_agent(
    role="Risk Assessment Judge",
    goal="Score risks based on realistic severity, likelihood, and impact word limit 150.",
    backstory=(
        "You evaluate cybersecurity risks using frameworks like CVSS, OWASP, and likelihood modelling. "
        "You assign severity labels (Low/Medium/High/Critical) and select top priority actions."
    ),
)
