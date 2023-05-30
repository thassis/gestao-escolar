"""Database ORM models for SQLAlchemy."""

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import sys
sys.path.append('../../../../')

from backend.core.domain.models.PeriodoLetivo import PeriodoLetivo

Base = declarative_base()

class PeriodoLetivoORM(Base):
    """PeriodoLetivo ORM class for SQLAlchemy."""
    __tablename__ = 'periodo_letivo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    class_shift = Column(String(100), nullable=False)
    dias_sem_aula = relationship("DiaSemAulaORM", backref="periodo_letivo")