from agents.base_agent_settings import create_agent
import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["CREWAI_ALLOW_LOCAL_MODE"] = "true"
os.environ["CREWAI_STORAGE_BACKEND"] = "memory"   # ⬅ key fix


blue_team_agent = create_agent(
    role="Blue Team Security Engineer",
    goal="Provide high-level defensive strategies to mitigate identified risks.",
    backstory=(
        "You design secure systems and defend against risks. "
        "Your responses should provide: short-term fixes, long-term solutions, and best practices within 150 words."
    ),
)
