from crewai import Task
import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["CREWAI_ALLOW_LOCAL_MODE"] = "true"
os.environ["CREWAI_STORAGE_BACKEND"] = "memory"   # ⬅ key fix

def create_judge_task(agent):
    return Task(
        description="Evaluate the red and blue team outputs and score risks objectively.",
        agent=agent,
        expected_output="A risk severity score matrix and prioritized issue list."
    )
