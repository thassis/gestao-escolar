"""Repository interface for domain layer."""

from abc import ABC, abstractmethod
from backend.core.domain.models import Aluno


class AlunoRepository(ABC):
    """Aluno repository interface for domain layer. It defines the methods
    for saving, retrieving, and deleting Aluno objects."""

    @abstractmethod
    def save(self, aluno: Aluno) -> Aluno:
        """Saves an Aluno object to the repository."""
        pass

    @abstractmethod
    def get_by_id(self, aluno_id: int) -> Aluno:
        """Retrieves an Aluno object from the repository by its ID."""
        pass

    @abstractmethod
    def delete(self, aluno: Aluno) -> None:
        """Deletes an Aluno object from the repository."""
        pass
