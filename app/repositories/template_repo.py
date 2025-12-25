"""Repository for templates and template exercises."""
from sqlalchemy.orm import Session

from app.models.template import Template, TemplateExercise


class TemplateRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_id: int | None, name: str, description: str | None = None) -> Template:
        t = Template(user_id=user_id, name=name, description=description)
        self.db.add(t)
        self.db.commit()
        self.db.refresh(t)
        return t

    def add_exercise(self, template: Template, exercise_id: int, order: int | None = None, sets: int | None = None, reps: int | None = None) -> TemplateExercise:
        te = TemplateExercise(template_id=template.id, exercise_id=exercise_id, order=order, sets=sets, reps=reps)
        self.db.add(te)
        self.db.commit()
        self.db.refresh(te)
        return te

    def get(self, template_id: int) -> Template | None:
        return self.db.query(Template).filter(Template.id == template_id).first()
