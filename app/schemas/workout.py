"""Pydantic schemas for workouts and sets."""
from datetime import datetime
from pydantic import BaseModel


class SetCreate(BaseModel):
    exercise_id: int
    reps: int | None = None
    weight: int | None = None
    rest_seconds: int | None = None
    order: int | None = None


class WorkoutCreate(BaseModel):
    user_id: int
    name: str | None = None
    date: datetime | None = None
    notes: str | None = None


class SetRead(BaseModel):
    id: int
    exercise_id: int
    reps: int | None = None
    weight: int | None = None

    model_config = {"from_attributes": True}


class WorkoutRead(BaseModel):
    id: int
    user_id: int
    date: datetime
    sets: list[SetRead] = []

    model_config = {"from_attributes": True}
