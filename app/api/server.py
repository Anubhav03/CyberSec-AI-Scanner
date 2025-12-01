# app/api/app.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as upload_router

app = FastAPI(
    title="CyberSec AI Backend",
    description="Backend for uploading repos and running security workflow.",
    version="0.1.0",
)

# CORS – allow frontend (Streamlit / hosted UI) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount our upload routes under /api
app.include_router(upload_router, prefix="/api")
