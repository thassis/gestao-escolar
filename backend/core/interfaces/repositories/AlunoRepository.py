"""Repository interface for domain layer.

- A Interface define as operações que o domínio precisa.
- A implementação das operações é feita fora, no adaptador.
- Domínio está desacoplado de qualquer implementação específica
"""

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

    @abstractmethod
    def get_by_name(self, aluno_name: str) -> list[Aluno]:
        """Retrieves an Aluno object from the repository by its name."""
        pass

    @abstractmethod
    def get_all_alunos(self) -> list[Aluno]:
        """Retrieves all Aluno objects from the repository."""
        pass

    @abstractmethod
    def get_alunos_paginated(self, offset, limit, name_like) -> list[Aluno]:
        """Retrieves a paginated list of Aluno objects from the repository."""
        pass
