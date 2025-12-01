from fastapi import APIRouter, HTTPException, Response
from pathlib import Path

router = APIRouter()

REPORTS_DIR = Path("./data/reports")

@router.get("/download/{report_name}")
def download_report(report_name: str):
    """Serve generated PDF or markdown report."""
    file_path = REPORTS_DIR / report_name

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Report not found")

    file_bytes = file_path.read_bytes()
    return Response(
        content=file_bytes,
        media_type="application/pdf" if report_name.endswith(".pdf") else "text/plain",
        headers={"Content-Disposition": f"attachment; filename={report_name}"},
    )
