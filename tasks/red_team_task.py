from crewai import Task

def create_red_team_task(agent):
    return Task(
        description="Analyze the summarized architecture and generate a red-team style attack plan.",
        agent=agent,
        expected_output="List of vulnerabilities, attack chains and exploit feasibility."
    )
