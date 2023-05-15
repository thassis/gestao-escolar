"""Database repositories module."""

from sqlalchemy.orm import Session
from backend.core.domain.models import Aluno
from backend.core.interfaces.repositories import AlunoRepository


class AlunoRepositoryPostgres(AlunoRepository):
    """Aluno repository class for PostgreSQL implementation."""

    def __init__(self, db: Session):
        """Initializes the repository with a database session."""
        self.db = db


    def save(self, aluno: Aluno) -> Aluno:
        """Saves an Aluno object to the database."""
        self.db.add(aluno)
        self.db.commit()
        self.db.refresh(aluno)
        return aluno


    def get_by_id(self, aluno_id: int) -> Aluno:
        """Retrieves an Aluno object from the database by its ID."""
        return self.db.query(Aluno).filter(Aluno.id == aluno_id).first()


    def delete(self, aluno: Aluno) -> None:
        """Deletes an Aluno object from the database."""
        self.db.delete(aluno)
        self.db.commit()
