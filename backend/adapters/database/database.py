"""Database ORM models for SQLAlchemy."""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base


# Create an engine to connect to a database
# Replace <user>, <password>, <host>, <port>, and <database> with your own values
engine = create_engine(
    'postgresql://<postgres>:<postgres>@<localhost>:<5450>/<postgres>',
    echo=True)


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


class ProfessorORM(Base):
    """Professor ORM class for SQLAlchemy."""
    __tablename__ = 'professor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)


Base.metadata.create_all(engine)
