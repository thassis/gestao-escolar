"""Repository interface for domain layer.

- A Interface define as operações que o domínio precisa.
- A implementação das operações é feita fora, no adaptador.
- Domínio está desacoplado de qualquer implementação específica
"""

from abc import ABC, abstractmethod
from backend.core.domain.models.Professor import Professor

class ProfessorRepository(ABC):
    """Professor repository interface for domain layer. It defines the methods
    for veryfing professor login credentials."""

    @abstractmethod
    def verify_login(self, professor_email: str, professor_password: str) -> bool | str:
        """Verifies professor login credentials."""
        pass

    @abstractmethod
    def save(self, professor: Professor) -> Professor:
        """Saves a Professor object to the repository."""
        pass

    @abstractmethod
    def delete(self, professor: Professor) -> None:
        """Deletes a Professor object from the repository."""
        pass

    @abstractmethod
    def get_by_id(self, professor_id: int) -> Professor:
        """Retrieves a Professor object from the repository by its ID."""
        pass

    @abstractmethod
    def get_by_name(self, professor_name: str) -> Professor:
        """Retrieves a Professor object from the repository by its name."""
        pass