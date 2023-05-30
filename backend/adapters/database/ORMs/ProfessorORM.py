"""Database ORM models for SQLAlchemy."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

import sys
sys.path.append('../../../../')

Base = declarative_base()

class ProfessorORM(Base):
    """Professor ORM class for SQLAlchemy."""
    __tablename__ = 'professor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    @staticmethod
    def from_professor(professor):
        """Converts a Professor object to a ProfessorORM object."""
        return ProfessorORM(
            name=professor.name,
            email=professor.email,
            password=professor.password
        )
