"""Simple analytics endpoints for progress and summaries."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.db.session import get_db
from app.models.workout import Workout, WorkoutSet

router = APIRouter()


@router.get("/weekly-volume/{user_id}")
def weekly_volume(user_id: int, db: Session = Depends(get_db)):
    """Return total volume (weight * reps) per day for the last 7 days."""
    now = datetime.utcnow()
    start = now - timedelta(days=7)
    workouts = db.query(Workout).filter(Workout.user_id == user_id, Workout.date >= start).all()
    per_day = {}
    for w in workouts:
        day = w.date.date().isoformat()
        total = 0
        for s in w.sets:
            if s.weight and s.reps:
                total += s.weight * (s.reps or 0)
        per_day.setdefault(day, 0)
        per_day[day] += total
    return {"weekly_volume": per_day}


@router.get("/monthly-sessions/{user_id}")
def monthly_sessions(user_id: int, db: Session = Depends(get_db)):
    """Return count of workout sessions per month for the last 6 months."""
    now = datetime.utcnow()
    start = now - timedelta(days=180)
    workouts = db.query(Workout).filter(Workout.user_id == user_id, Workout.date >= start).all()
    per_month = {}
    for w in workouts:
        key = f"{w.date.year}-{w.date.month:02d}"
        per_month.setdefault(key, 0)
        per_month[key] += 1
    return {"monthly_sessions": per_month}
