"""Pydantic schemas for goals."""
from datetime import datetime
from pydantic import BaseModel


class GoalCreate(BaseModel):
    user_id: int
    title: str
    kind: str
    target: int | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None


class GoalRead(BaseModel):
    id: int
    user_id: int
    title: str
    kind: str
    target: int | None = None
    achieved: bool

    model_config = {"from_attributes": True}
