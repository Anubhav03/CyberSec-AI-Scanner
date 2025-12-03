from agents.base_agent_settings import create_agent
import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["CREWAI_ALLOW_LOCAL_MODE"] = "true"
os.environ["CREWAI_STORAGE_BACKEND"] = "memory"   # ⬅ key fix


compliance_agent = create_agent(
    role="Compliance Mapping Specialist",
    goal="Translate vulnerabilities into compliance requirements and best-practice checklists with word limit 150.",
    backstory=(
        "You specialize in OWASP Top 10, ISO 27001, NIST, PCI-DSS, and secure software lifecycle standards. "
        "Map risks to compliance concerns and produce a simple actionable checklist."
    ),
)
