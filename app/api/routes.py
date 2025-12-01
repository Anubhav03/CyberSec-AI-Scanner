import shutil
import uuid
from pathlib import Path
from fastapi import APIRouter, UploadFile, File
from main import run_full_security_workflow
import tempfile
import zipfile
import tarfile

router = APIRouter()

@router.post("/upload")
async def upload_repo(file: UploadFile = File(...)):
    # Create a unique temp directory for the repo
    session_id = str(uuid.uuid4())
    temp_dir = Path(tempfile.gettempdir()) / session_id
    temp_dir.mkdir(parents=True, exist_ok=True)

    saved_file_path = temp_dir / file.filename

    # Save uploaded file
    with open(saved_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract if ZIP or TAR
    extract_path = temp_dir / "repo"
    extract_path.mkdir(parents=True, exist_ok=True)

    if saved_file_path.suffix == ".zip":
        with zipfile.ZipFile(saved_file_path, "r") as zip_ref:
            zip_ref.extractall(extract_path)
    elif saved_file_path.suffix in [".tar", ".gz", ".tgz"]:
        with tarfile.open(saved_file_path, "r:*") as tar_ref:
            tar_ref.extractall(extract_path)
    else:
        return {"error": "Only ZIP or TAR files are supported"}

    # Run your scanner
    result = run_full_security_workflow(str(extract_path))

    return {
        "session_id": session_id,
        "original_filename": file.filename,
        "status": "success",
        "analysis": result
    }



def cleanup(path: str):
    try:
        shutil.rmtree(path)
    except Exception:
        pass
