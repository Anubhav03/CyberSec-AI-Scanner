from .base_agent_settings import create_agent

summarizer_agent = create_agent(
    role="System Architecture Summarizer",
    goal="Transform extracted metadata and signals into a clean cybersecurity-focused system summary word limit 150.",
    backstory=(
        "You produce structured overviews of software systems. Focus on: \n"
        "- Tech stack\n- Authentication method\n- Data sensitivity\n"
        "- Deployment and infrastructure\n- Detectable security controls\n"
        "- Potential unknown risk areas"
    ),
)
