from pathlib import Path
from typing import Any

# ---- Pipeline imports ----
from pipeline.scanner import scan_repository
from pipeline.chunker import chunk_files
from pipeline.vector_store import build_vector_store

# ---- Task imports ----
from tasks.repo_scan_task import create_repo_scan_task
from tasks.summarization_task import create_summarization_task
from tasks.red_team_task import create_red_team_task
from tasks.blue_team_task import create_blue_team_task
from tasks.judge_task import create_judge_task
from tasks.compliance_task import create_compliance_task

# ---- Agents ----
from agents.repo_scanner_agent import repo_scanner_agent
from agents.summarizer_agent import summarizer_agent
from agents.red_team_agent import red_team_agent
from agents.blue_team_agent import blue_team_agent
from agents.judge_agent import judge_agent
from agents.compliance_agent import compliance_agent

# ---- Report builder ----
#from reports.generator import build_full_report
from crewai import Crew


def run_task(task):
    """Runs a CrewAI task safely and returns plain text."""
    print(f"➡ Running: {task.description}")
    result = task.execute()
    
    if hasattr(result, "output"):
        return result.output
    if hasattr(result, "result"):
        return result.result
    if hasattr(result, "response"):
        return result.response

    return str(result)


def run_full_security_workflow(repo_path: str):
    repo_name = Path(repo_path).name
    print(f"🔍 Starting security workflow for: {repo_name}")

    scanned_files = scan_repository(repo_path)

    chunks = chunk_files(scanned_files)
    build_vector_store(chunks)

    # ---- Create task pipeline ----
    repo_task = create_repo_scan_task(repo_scanner_agent, scanned_files)

    summary_task = create_summarization_task(summarizer_agent)

    red_task = create_red_team_task(red_team_agent)

    blue_task = create_blue_team_task(blue_team_agent)

    judge_task = create_judge_task(judge_agent)

    compliance_task = create_compliance_task(compliance_agent)


    crew = Crew(
        agents=[
            repo_scanner_agent,
            summarizer_agent,
            red_team_agent,
            blue_team_agent,
            judge_agent,
            compliance_agent
        ],
        tasks=[
            repo_task,
            summary_task,
            red_task,
            blue_task,
            judge_task,
            compliance_task
        ],
        verbose=True
    )

    print("🚀 Running crew workflow...")
    final_output = crew.kickoff()

    print("🎉 Workflow complete!")

    print("\n===== FINAL REPORT OUTPUT =====\n")
    print(final_output)

    return final_output



if __name__ == "__main__":
    run_full_security_workflow("./data/sample_repo")
