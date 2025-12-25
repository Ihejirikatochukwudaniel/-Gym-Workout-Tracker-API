"""Pydantic schemas for user-related payloads."""
from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    username: str | None = None


class UserRead(BaseModel):
    id: int
    email: EmailStr
    username: str | None = None
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: str | None = None

    model_config = {"from_attributes": True}
