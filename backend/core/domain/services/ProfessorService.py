"""Domain layer services module. It follows hexagonal architecture principles.

- O serviço está desacoplado de qualquer implementação específica,
  tal como DB ou ORM
"""

from backend.core.domain.models.Professor import Professor
from backend.core.interfaces.repositories.ProfessorRepository import ProfessorRepository


class ProfessorService:
    """Professor service class for domain layer. It provides methods for
    verifying professor login credentials. It takes a professor_repository
    object as a dependency."""

    def __init__(self, professor_repository: ProfessorRepository):
        """Initializes the service with a ProfessorRepository object."""
        self.professor_repository = professor_repository

    def login(self, email, password):
        """Verifies professor login credentials."""
        login = self.professor_repository.verify_login(email, password)
        return login

    def create_professor(self, name, email, password):
        """Creates a new Professor object and saves it to the repository.
        When creating a new Professor object, the ID does not need to be
        provided, as it is generated automatically by the repository."""
        professor = Professor(
            id=None,
            name=name,
            email=email,
            password=password
        )
        self.professor_repository.save(professor)
        if professor is not None:
            return professor
        return False

    def update_professor(self, professor_id, name=None, email=None,
                        password=None):
        """Updates an existing Professor object and saves it to the repository."""
        professor = self.professor_repository.get_by_id(professor_id)
        if professor_id is not None:
            professor.id = professor_id
        if name is not None:
            professor.name = name
        if email is not None:
            professor.email = email
        if password is not None:
            professor.password = password
        self.professor_repository.save(professor)
        if professor is not None:
            return professor
        return False

    def remove_professor(self, professor_id):
        """Removes an existing Professor object from the repository."""
        professor = self.professor_repository.get_by_id(professor_id)
        self.professor_repository.delete(professor)

    def get_professor_by_name(self, professor_name):
        """Retrieves an existing Professor object from the repository."""
        professor = self.professor_repository.get_by_name(professor_name)
        return professor