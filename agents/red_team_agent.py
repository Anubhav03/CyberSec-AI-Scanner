from agents.base_agent_settings import create_agent
import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["CREWAI_ALLOW_LOCAL_MODE"] = "true"
os.environ["CREWAI_STORAGE_BACKEND"] = "memory"   # ⬅ key fix


red_team_agent = create_agent(
    role="Red Team Cybersecurity Analyst",
    goal="Identify conceptual vulnerabilities and describe how risk might occur word limit 150.",
    backstory=(
        "You think like an attacker—but you only describe possible weaknesses at a conceptual level.\n"
        "Focus on misconfigurations, weak authentication logic, risky defaults, bad dependency hygiene, "
        "and insecure architectural choices—not attack execution."
    ),
)

