"""Repository for goals."""
from sqlalchemy.orm import Session

from app.models.goal import Goal


class GoalRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_id: int, title: str, kind: str, target: int | None = None, start_date=None, end_date=None) -> Goal:
        g = Goal(user_id=user_id, title=title, kind=kind, target=target, start_date=start_date, end_date=end_date)
        self.db.add(g)
        self.db.commit()
        self.db.refresh(g)
        return g

    def get(self, goal_id: int) -> Goal | None:
        return self.db.query(Goal).filter(Goal.id == goal_id).first()

    def list_for_user(self, user_id: int):
        return self.db.query(Goal).filter(Goal.user_id == user_id).all()
