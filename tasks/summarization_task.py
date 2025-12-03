from crewai import Task
import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["CREWAI_ALLOW_LOCAL_MODE"] = "true"
os.environ["CREWAI_STORAGE_BACKEND"] = "memory"   # ⬅ key fix

def create_summarization_task(agent):
    return Task(
        description="Summarize the repository scan into a cybersecurity architecture report.",
        agent=agent,
        expected_output="A structured cybersecurity-oriented architecture summary."
    )
