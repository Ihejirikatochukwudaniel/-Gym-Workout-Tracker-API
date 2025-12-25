"""Repository for workouts and sets."""
from sqlalchemy.orm import Session
from typing import List

from app.models.workout import Workout, WorkoutSet


class WorkoutRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, *, user_id: int, name: str | None = None, date=None, notes: str | None = None):
        workout = Workout(user_id=user_id, name=name, date=date, notes=notes)
        self.db.add(workout)
        self.db.commit()
        self.db.refresh(workout)
        return workout

    def get(self, workout_id: int) -> Workout | None:
        return self.db.query(Workout).filter(Workout.id == workout_id).first()

    def delete(self, workout: Workout):
        self.db.delete(workout)
        self.db.commit()

    def add_set(self, workout: Workout, *, exercise_id: int, reps: int | None = None, weight: int | None = None, rest_seconds: int | None = None, order: int | None = None) -> WorkoutSet:
        wset = WorkoutSet(workout_id=workout.id, exercise_id=exercise_id, reps=reps, weight=weight, rest_seconds=rest_seconds, order=order)
        self.db.add(wset)
        self.db.commit()
        self.db.refresh(wset)
        return wset
