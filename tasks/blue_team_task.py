from crewai import Task
import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["CREWAI_ALLOW_LOCAL_MODE"] = "true"
os.environ["CREWAI_STORAGE_BACKEND"] = "memory"   # ⬅ key fix

def create_blue_team_task(agent):
    return Task(
        description="Generate mitigations and defensive strategies for the identified attack paths.",
        agent=agent,
        expected_output="Security patches, hardening measures, IAM recommendations."
    )
