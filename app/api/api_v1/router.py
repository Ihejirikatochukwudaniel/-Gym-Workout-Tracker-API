"""API router for v1 endpoints."""
from fastapi import APIRouter

from app.api.api_v1.endpoints import auth, workouts, templates, goals, analytics

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(workouts.router, prefix="/workouts", tags=["workouts"])
api_router.include_router(templates.router, prefix="/templates", tags=["templates"])
api_router.include_router(goals.router, prefix="/goals", tags=["goals"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
