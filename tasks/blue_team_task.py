from crewai import Task

def create_blue_team_task(agent):
    return Task(
        description="Generate mitigations and defensive strategies for the identified attack paths.",
        agent=agent,
        expected_output="Security patches, hardening measures, IAM recommendations."
    )
