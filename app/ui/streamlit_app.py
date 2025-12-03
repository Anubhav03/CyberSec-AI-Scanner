# app/ui/streamlit_app.py

import os
import sys
import json
from pathlib import Path

import streamlit as st
import requests

# Ensure backend path access (optional but helpful when local-running)
ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

# Backend endpoint (supports deployment override)
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
UPLOAD_ENDPOINT = f"{BACKEND_URL}/api/upload"

# UI settings
st.set_page_config(
    page_title="CyberSec AI Scanner",
    page_icon="🛡️",
    layout="wide",
)

st.title("🛡️ CyberSec AI Scanner")
st.write("Upload a zipped repository and run a full multi-agent cybersecurity analysis.")

uploaded_file = st.file_uploader(
    "📁 Upload project file (.zip or .tar.gz)",
    type=["zip", "tar", "gz", "tgz"]
)

# Store results across reruns
if "last_result" not in st.session_state:
    st.session_state.last_result = None


# ------------------ SEND FILE TO API ------------------
if uploaded_file and st.button("🚀 Run Scan", type="primary"):
    with st.spinner("🔍 Uploading and analyzing repository... Please wait..."):
        try:
            files = {"file": (uploaded_file.name, uploaded_file.getvalue())}

            response = requests.post(UPLOAD_ENDPOINT, files=files, timeout=600)

            if response.status_code == 200:
                st.session_state.last_result = response.json()
                st.success("✔️ Scan completed successfully!")
            else:
                st.error(f"❌ Backend error: {response.status_code}")
                st.code(response.text)

        except Exception as e:
            st.error(f"❌ Network or request error: {e}")


# ------------------ RENDER FUNCTION ------------------
def render_analysis(content):
    """Smart formatter for AI workflow results."""

    if isinstance(content, str):
        st.markdown(content)
        return

    if isinstance(content, dict):
        # Display readable section first if exists
        text_blocks = ["final_report", "raw", "summary", "report", "human_readable"]

        for key in text_blocks:
            if key in content and isinstance(content[key], str):
                st.subheader("🧠 Final Analysis Summary")
                st.markdown(content[key])
                break

        # Agent task output sections
        if "tasks_output" in content and isinstance(content["tasks_output"], list):
            st.subheader("📌 Agent Task Breakdown")
            for idx, task in enumerate(content["tasks_output"]):
                with st.expander(f"🔹 Task {idx+1}: {task.get('name', 'Unnamed Task')}"):
                    st.markdown(task.get("raw") or "**No readable text**")

        # Show entire JSON for transparency
        st.subheader("🗂 Full Structured Output (JSON)")
        st.json(content)
        return

    if isinstance(content, list):
        st.subheader("📄 Multi-Section Output:")
        for i, section in enumerate(content):
            with st.expander(f"Section {i+1}"):
                render_analysis(section)
        return

    st.code(str(content))


# ------------------ DISPLAY RESULTS ------------------
if st.session_state.last_result:
    result = st.session_state.last_result

    st.subheader("📌 Scan Metadata")
    st.write(f"**Session ID:** `{result.get('session_id')}`")
    st.write(f"**Uploaded File:** `{result.get('original_filename')}`")

    st.divider()
    st.subheader("📄 Security Report")

    analysis = result.get("analysis")

    render_analysis(analysis)
