"""Pydantic schemas for templates."""
from pydantic import BaseModel


class TemplateExerciseCreate(BaseModel):
    exercise_id: int
    order: int | None = None
    sets: int | None = None
    reps: int | None = None


class TemplateCreate(BaseModel):
    user_id: int | None = None
    name: str
    description: str | None = None
    exercises: list[TemplateExerciseCreate] | None = None


class TemplateRead(BaseModel):
    id: int
    user_id: int | None = None
    name: str
    description: str | None = None

    model_config = {"from_attributes": True}
