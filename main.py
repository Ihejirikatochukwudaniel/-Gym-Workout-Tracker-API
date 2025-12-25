"""Top-level compatibility importer so `uvicorn main:app` works.

This simply re-exports the FastAPI app from `app.main`.
"""
from app.main import app  # re-export for convenience
