"""Service layer for goals."""
from sqlalchemy.orm import Session

from app.repositories.goal_repo import GoalRepository


class GoalService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = GoalRepository(db)

    def create_goal(self, user_id: int, title: str, kind: str, target: int | None = None, start_date=None, end_date=None):
        return self.repo.create(user_id=user_id, title=title, kind=kind, target=target, start_date=start_date, end_date=end_date)

    def list_goals(self, user_id: int):
        return self.repo.list_for_user(user_id)
