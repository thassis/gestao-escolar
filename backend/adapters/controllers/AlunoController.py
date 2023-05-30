"""This module implements the Aluno controller to enable the communication
between the frontend adapter and the domain layer without exposing the
database adapter to the frontend adapter.
"""

from backend.core.domain.services.AlunoService import AlunoService
from backend.adapters.database.repositories.AlunoRepository import AlunoRepositoryPostgres

from backend.adapters.database.DatabaseSession import DatabaseSession

class AlunoController:
    """Aluno controller class for adapters. It provides methods for
    creating, updating, and retrieving Aluno objects. It takes a db object,
    an AlunoRepository object, and an AlunoService object as dependencies.\\
    This class enables the communication between the frontend adapter and
    the domain layer, without exposing the database adapter to the
    frontend adapter.
    """
    def __init__(self) -> None:
        """Initializes the controller with a db object, an AlunoRepository
        object, and an AlunoService object."""
        database = DatabaseSession()
        self.database_session = database.get_db_session()
        self.aluno_repository = AlunoRepositoryPostgres(self.database_session)
        self.aluno_service = AlunoService(self.aluno_repository)


    def get_alunos_by_name(self, name):
        """Retrieves a list of Aluno objects from the repository by name."""
        return self.aluno_service.get_alunos_by_name(name)
        # return True

    def get_all_alunos(self):
        """Retrieves a list of all Aluno objects from the repository."""
        return self.aluno_service.get_all_alunos()

    def get_alunos_paginated(self, offset, limit, name_like):
        """Retrieves a list of Aluno objects from the repository
        in a paginated way.
        """
        return self.aluno_service.get_alunos_paginated(offset, limit, name_like)

    def create(self, name, born_date, address, tutor_name,
                    tutor_phone, class_shift):
        """Creates a new Aluno object and saves it to the repository."""
        return self.aluno_service.create_aluno(name, born_date, address,
                                               tutor_name, tutor_phone,
                                               class_shift)
        # return True

    def update(self, aluno_id, name=None, born_date=None,
                        address=None, tutor_name=None, tutor_phone=None,
                        class_shift=None):
        """Updates an existing Aluno object and saves it to the repository."""
        return self.aluno_service.update_aluno(aluno_id, name, born_date,
                       address, tutor_name, tutor_phone,
                       class_shift)
        # return True

    def remove(self, aluno_id):
        """Removes an existing Aluno object from the repository."""
        return self.aluno_service.remove_aluno(aluno_id)
        # return True