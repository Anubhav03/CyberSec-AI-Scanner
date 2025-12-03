from crewai import Task
from typing import List, Dict
import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["CREWAI_ALLOW_LOCAL_MODE"] = "true"
os.environ["CREWAI_STORAGE_BACKEND"] = "memory"   # ⬅ key fix


def extract_dependency_signals(files: List[Dict]) -> str:
    """Extract basic signals about repo tech stack and dependencies."""
    signals = []

    for file in files:
        name = file["filename"].lower()

        if "requirements" in name or "pipfile" in name:
            signals.append("Python dependency file detected")
        elif "package.json" in name:
            signals.append("Node.js project detected")
        elif "go.mod" in name:
            signals.append("Go modules detected")
        elif "pom.xml" in name:
            signals.append("Java Maven detected")
        elif "build.gradle" in name:
            signals.append("Java/Android Gradle detected")

    return "\n".join(signals) if signals else "Unknown stack"


def create_repo_scan_task(agent, scanned_files: List[Dict]) -> Task:
    """Create task for repo scanning agent."""

    extracted_signals = extract_dependency_signals(scanned_files)

    return Task(
        description=(
            "Analyze the following repository structure and return a structured metadata summary:"
            f"\n\nStack Indicators:\n{extracted_signals}"
        ),
        agent=agent,
        # 👇 No context list needed here
        expected_output="Structured repository metadata including code layout"
    )
