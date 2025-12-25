"""Configuration for the application."""
from __future__ import annotations
import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = "Gym Workout Tracker API"
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

# SQLite for development; change to PostgreSQL in production
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")

def get_access_token_expires() -> timedelta:
    return timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
