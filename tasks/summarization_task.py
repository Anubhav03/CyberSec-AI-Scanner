from crewai import Task

def create_summarization_task(agent):
    return Task(
        description="Summarize the repository scan into a cybersecurity architecture report.",
        agent=agent,
        expected_output="A structured cybersecurity-oriented architecture summary."
    )
