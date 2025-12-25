"""Workout and Set ORM models."""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.db.base import Base


class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    name = Column(String(200), nullable=True)
    date = Column(DateTime, default=datetime.utcnow, index=True)
    notes = Column(Text, nullable=True)
    template_id = Column(Integer, ForeignKey("templates.id"), nullable=True)

    sets = relationship("WorkoutSet", back_populates="workout", cascade="all, delete-orphan")
    user = relationship("User", backref="workouts")


class WorkoutSet(Base):
    __tablename__ = "workout_sets"

    id = Column(Integer, primary_key=True, index=True)
    workout_id = Column(Integer, ForeignKey("workouts.id"), nullable=False, index=True)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)
    reps = Column(Integer, nullable=True)
    weight = Column(Integer, nullable=True)
    rest_seconds = Column(Integer, nullable=True)
    order = Column(Integer, nullable=True)

    workout = relationship("Workout", back_populates="sets")
    exercise = relationship("Exercise")
