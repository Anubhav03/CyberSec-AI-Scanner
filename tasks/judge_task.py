from crewai import Task

def create_judge_task(agent):
    return Task(
        description="Evaluate the red and blue team outputs and score risks objectively.",
        agent=agent,
        expected_output="A risk severity score matrix and prioritized issue list."
    )
