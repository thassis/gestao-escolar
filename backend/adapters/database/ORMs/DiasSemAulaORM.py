

"""Database ORM models for SQLAlchemy."""

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

import sys
sys.path.append('../../../../')

from backend.core.domain.models.DiasSemAula import DiaSemAula

Base = declarative_base()

class DiaSemAulaORM(Base):
    """DiaSemAula ORM class for SQLAlchemy."""
    __tablename__ = 'dia_sem_aula'

    id = Column(Integer, primary_key=True, autoincrement=True)
    periodo_letivo_id = Column(Integer, ForeignKey('periodo_letivo.id'), nullable=False)
    date = Column(Date, nullable=False)
    reason = Column(String(100), nullable=False)