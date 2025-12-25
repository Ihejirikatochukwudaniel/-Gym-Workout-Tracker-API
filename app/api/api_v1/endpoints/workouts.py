"""Workouts endpoints: create workout, add set, get workout."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.services.workout_service import WorkoutService
from app.db.session import get_db
from app.repositories.user_repo import UserRepository
from app.schemas.user import UserRead

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_workout(payload: dict, db: Session = Depends(get_db)):
    svc = WorkoutService(db)
    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(status_code=400, detail="user_id is required")
    workout = svc.create_workout(user_id=user_id, name=payload.get("name"), notes=payload.get("notes"))
    return {"id": workout.id}


@router.post("/{workout_id}/sets", status_code=status.HTTP_201_CREATED)
def add_set(workout_id: int, payload: dict, db: Session = Depends(get_db)):
    svc = WorkoutService(db)
    try:
        wset = svc.add_set(workout_id=workout_id, exercise_id=payload.get("exercise_id"), reps=payload.get("reps"), weight=payload.get("weight"), rest_seconds=payload.get("rest_seconds"), order=payload.get("order"))
    except ValueError:
        raise HTTPException(status_code=404, detail="Workout not found")
    return {"id": wset.id}


@router.get("/{workout_id}")
def get_workout(workout_id: int, db: Session = Depends(get_db)):
    svc = WorkoutService(db)
    workout = svc.repo.get(workout_id)
    if not workout:
        raise HTTPException(status_code=404, detail="Not found")
    return {
        "id": workout.id,
        "user_id": workout.user_id,
        "date": workout.date,
        "sets": [{"id": s.id, "exercise_id": s.exercise_id, "reps": s.reps, "weight": s.weight} for s in workout.sets],
    }
