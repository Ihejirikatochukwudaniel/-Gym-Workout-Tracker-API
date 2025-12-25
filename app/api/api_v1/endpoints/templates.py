"""Endpoints for managing templates."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.services.template_service import TemplateService
from app.schemas.template import TemplateCreate, TemplateRead, TemplateExerciseCreate
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=TemplateRead, status_code=status.HTTP_201_CREATED)
def create_template(payload: TemplateCreate, db: Session = Depends(get_db)):
    svc = TemplateService(db)
    t = svc.create_template(user_id=payload.user_id, name=payload.name, description=payload.description)
    # optionally add exercises
    if payload.exercises:
        for ex in payload.exercises:
            svc.add_exercise(t.id, exercise_id=ex.exercise_id, order=ex.order, sets=ex.sets, reps=ex.reps)
    return t


@router.post("/{template_id}/exercises", status_code=status.HTTP_201_CREATED)
def add_exercise(template_id: int, payload: TemplateExerciseCreate, db: Session = Depends(get_db)):
    svc = TemplateService(db)
    try:
        te = svc.add_exercise(template_id=template_id, exercise_id=payload.exercise_id, order=payload.order, sets=payload.sets, reps=payload.reps)
    except ValueError:
        raise HTTPException(status_code=404, detail="Template not found")
    return {"id": te.id}
