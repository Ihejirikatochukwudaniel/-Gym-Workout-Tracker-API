"""Service layer with business logic for workouts."""
from sqlalchemy.orm import Session
from typing import List

from app.repositories.workout_repo import WorkoutRepository
from app.models.workout import Workout


class WorkoutService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = WorkoutRepository(db)

    def create_workout(self, user_id: int, name: str | None = None, date=None, notes: str | None = None) -> Workout:
        return self.repo.create(user_id=user_id, name=name, date=date, notes=notes)

    def add_set(self, workout_id: int, exercise_id: int, reps: int | None = None, weight: int | None = None, rest_seconds: int | None = None, order: int | None = None):
        workout = self.repo.get(workout_id)
        if not workout:
            raise ValueError("Workout not found")
        return self.repo.add_set(workout, exercise_id=exercise_id, reps=reps, weight=weight, rest_seconds=rest_seconds, order=order)
