"""Seed script to populate default exercises into the DB."""
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.exercise import Exercise


DEFAULT_EXERCISES = [
    {"name": "Squat", "category": "Strength", "muscle_group": "Quadriceps"},
    {"name": "Deadlift", "category": "Strength", "muscle_group": "Posterior Chain"},
    {"name": "Bench Press", "category": "Strength", "muscle_group": "Chest"},
    {"name": "Pull Up", "category": "Strength", "muscle_group": "Back"},
]


def seed():
    db: Session = SessionLocal()
    try:
        for item in DEFAULT_EXERCISES:
            exists = db.query(Exercise).filter(Exercise.name == item["name"]).first()
            if not exists:
                db.add(Exercise(**item))
        db.commit()
        print("Seeded exercises")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
