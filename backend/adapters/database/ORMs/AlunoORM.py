"""Database ORM models for SQLAlchemy."""

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

import sys
sys.path.append('../../../../')

from backend.core.domain.models.Aluno import Aluno

Base = declarative_base()

class AlunoORM(Base):
    """Aluno ORM class for SQLAlchemy."""
    __tablename__ = 'aluno'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    born_date = Column(Date, nullable=False)
    address = Column(String(200), nullable=False)
    tutor_name = Column(String(100), nullable=False)
    tutor_phone = Column(String(20), nullable=False)
    class_shift = Column(String(20), nullable=False)

    @staticmethod
    def from_aluno(aluno):
        """Converts an Aluno object to an AlunoORM object."""
        return AlunoORM(
            name=aluno.name,
            born_date=aluno.born_date,
            address=aluno.address,
            tutor_name=aluno.tutor_name,
            tutor_phone=aluno.tutor_phone,
            class_shift=aluno.class_shift
        )

    @staticmethod
    def to_aluno(aluno_orm):
        """Converts an AlunoORM object to an Aluno object."""
        return Aluno(
            id=aluno_orm.id,
            name=aluno_orm.name,
            born_date=aluno_orm.born_date,
            address=aluno_orm.address,
            tutor_name=aluno_orm.tutor_name,
            tutor_phone=aluno_orm.tutor_phone,
            class_shift=aluno_orm.class_shift
        )