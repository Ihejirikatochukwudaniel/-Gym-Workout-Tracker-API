"""Endpoints for managing goals."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.services.goal_service import GoalService
from app.schemas.goal import GoalCreate, GoalRead
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=GoalRead, status_code=status.HTTP_201_CREATED)
def create_goal(payload: GoalCreate, db: Session = Depends(get_db)):
    svc = GoalService(db)
    g = svc.create_goal(user_id=payload.user_id, title=payload.title, kind=payload.kind, target=payload.target, start_date=payload.start_date, end_date=payload.end_date)
    return g


@router.get("/user/{user_id}", response_model=list[GoalRead])
def list_goals(user_id: int, db: Session = Depends(get_db)):
    svc = GoalService(db)
    return svc.list_goals(user_id)
