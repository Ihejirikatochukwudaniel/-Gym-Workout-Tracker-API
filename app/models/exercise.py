"""Exercise library model (seeded)."""
from sqlalchemy import Column, Integer, String, Text

from app.db.base import Base


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, unique=True)
    category = Column(String(100), nullable=True)
    muscle_group = Column(String(100), nullable=True)
    description = Column(Text, nullable=True)
