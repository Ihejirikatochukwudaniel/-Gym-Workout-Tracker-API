"""Service layer for templates."""
from sqlalchemy.orm import Session

from app.repositories.template_repo import TemplateRepository


class TemplateService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = TemplateRepository(db)

    def create_template(self, user_id: int | None, name: str, description: str | None = None):
        return self.repo.create(user_id=user_id, name=name, description=description)

    def add_exercise(self, template_id: int, exercise_id: int, order: int | None = None, sets: int | None = None, reps: int | None = None):
        template = self.repo.get(template_id)
        if not template:
            raise ValueError("Template not found")
        return self.repo.add_exercise(template, exercise_id=exercise_id, order=order, sets=sets, reps=reps)
