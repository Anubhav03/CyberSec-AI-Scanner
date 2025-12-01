from crewai import Task

def create_compliance_task(agent):
    return Task(
        description="Map discovered risks to compliance frameworks (OWASP, NIST, GDPR, ISO27001).",
        agent=agent,
        expected_output="Compliance alignment report and missing control mapping."
    )
