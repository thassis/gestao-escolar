"""This module implements the Professor controller to enable the communication
between the frontend adapter and the domain layer without exposing the
database adapter to the frontend adapter.
"""

from backend.core.domain.services.ProfessorService import ProfessorService
from backend.adapters.database.repositories.ProfessorRepository import ProfessorRepositoryPostgres

from backend.adapters.database.DatabaseSession import DatabaseSession

class ProfessorController:
    """Professor controller class for adapters. It provides methods for
    creating, updating, and retrieving Professor objects. It takes a db object,
    an ProfessorRepository object, and an ProfessorService object as dependencies.\\
    This class enables the communication between the frontend adapter and
    the domain layer, without exposing the database adapter to the
    frontend adapter.
    """
    def __init__(self,) -> None:
        """Initializes the controller with a db object, an ProfessorRepository
        object, and an ProfessorService object."""
        database = DatabaseSession()
        self.database_session = database.get_db_session()
        self.professor_repository = ProfessorRepositoryPostgres(self.database_session)
        self.professor_service = ProfessorService(self.professor_repository)

    def login(self, email, password):
        """Verifies professor login credentials."""
        print("recebido controller: ", email, password) # TODO: Remove later
        return self.professor_service.login(email, password)
        # return True

    def create(self, name, email, password):
        """Creates a new Professor object and saves it to the repository."""
        return self.professor_service.create_professor(name, email, password)
        # return True

    def update(self, professor_id, name=None, email=None,
                        password=None):
        """Updates an existing Professor object and saves it to the repository."""
        return self.professor_service.update_professor(professor_id, name, email, password)
        # return True

    def remove(self, professor_id):
        """Removes an existing Professor object from the repository."""
        return self.professor_service.remove_professor(professor_id)
        # return True