"""Authentication service: business logic for registering and authenticating users."""
from datetime import timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import JWTError

from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate, Token
from app.core import security, config
from app.db.session import get_db


class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.users = UserRepository(db)

    def register(self, *, user_in: UserCreate):
        existing = self.users.get_by_email(user_in.email)
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed = security.hash_password(user_in.password)
        user = self.users.create(email=user_in.email, hashed_password=hashed, username=user_in.username)
        return user

    def authenticate(self, *, email: str, password: str):
        user = self.users.get_by_email(email)
        if not user:
            return None
        if not security.verify_password(password, user.hashed_password):
            return None
        return user

    def create_token(self, user_id: int, expires_delta: Optional[timedelta] = None) -> Token:
        token = security.create_access_token(subject=str(user_id), expires_delta=expires_delta)
        return Token(access_token=token)


def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(db)
