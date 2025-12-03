from crewai import Task
import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["CREWAI_ALLOW_LOCAL_MODE"] = "true"
os.environ["CREWAI_STORAGE_BACKEND"] = "memory"   # ⬅ key fix

def create_red_team_task(agent):
    return Task(
        description="Analyze the summarized architecture and generate a red-team style attack plan.",
        agent=agent,
        expected_output="List of vulnerabilities, attack chains and exploit feasibility."
    )
