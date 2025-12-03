from crewai import Task
import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["CREWAI_ALLOW_LOCAL_MODE"] = "true"
os.environ["CREWAI_STORAGE_BACKEND"] = "memory"   # ⬅ key fix

def create_compliance_task(agent):
    return Task(
        description="Map discovered risks to compliance frameworks (OWASP, NIST, GDPR, ISO27001).",
        agent=agent,
        expected_output="Compliance alignment report and missing control mapping."
    )
