"""Domain layer services module. It follows hexagonal architecture principles.

- O serviço está desacoplado de qualquer implementação específica,
  tal como DB ou ORM
"""

from backend.core.domain.models.Aluno import Aluno
from backend.core.interfaces.repositories.AlunoRepository import AlunoRepository

class AlunoService:
    """Aluno service class for domain layer. It provides methods for
    creating, updating, and removing Aluno objects. It takes an
    aluno_repository object as a dependency."""

    def __init__(self, aluno_repository: AlunoRepository):
        """Initializes the service with an AlunoRepository object."""
        self.aluno_repository = aluno_repository

    def create_aluno(self, name, born_date, address, tutor_name,
                    tutor_phone, class_shift):
        """Creates a new Aluno object and saves it to the repository.
        When creating a new Aluno object, the ID does not need to be
        specified, since it is generated automatically by the database.
        """
        aluno = Aluno(
            id=None,
            name=name,
            born_date=born_date,
            address=address,
            tutor_name=tutor_name,
            tutor_phone=tutor_phone,
            class_shift=class_shift
        )
        aluno = self.aluno_repository.save(aluno)
        if isinstance(aluno, str): # if aluno is not found
            return aluno
        return aluno


    def update_aluno(self, aluno_id, name=None, born_date=None,
                        address=None, tutor_name=None, tutor_phone=None,
                        class_shift=None):
        """Updates an existing Aluno object and saves it to the repository."""
        aluno = self.aluno_repository.get_by_id(aluno_id)
        if isinstance(aluno, str): # if aluno is not found
            return aluno

        if name is not None:
            aluno.name = name
        if born_date is not None:
            aluno.born_date = born_date
        if address is not None:
            aluno.address = address
        if tutor_name is not None:
            aluno.tutor_name = tutor_name
        if tutor_phone is not None:
            aluno.tutor_phone = tutor_phone
        if class_shift is not None:
            aluno.class_shift = class_shift
        self.aluno_repository.save(aluno)
        return aluno


    def remove_aluno(self, aluno_id):
        """Removes an existing Aluno object from the repository."""
        aluno = self.aluno_repository.get_by_id(aluno_id)
        message = self.aluno_repository.delete(aluno)
        return message


    def get_alunos_by_name(self, aluno_name: str) -> dict:
        """Retrieves one or more existing Aluno object from the repository.
        Returns a dictionary of alunos, where every aluno object is a
        dictionary itself.\\
        Args:
            aluno_name (str): The name of the aluno to be retrieved.
        Returns:
            alunos_dict (dict): A dictionary of alunos.
        """
        alunos = self.aluno_repository.get_by_name(aluno_name)

        # get all alunos and change it to a dictionary of alunos
        alunos_dict = {'Aluno': []} # {'Aluno': [{'id': 1, name: 'joao',...}, aluno2, ...]}
        for aluno in alunos:
            alunos_dict['Aluno'].append(aluno.__dict__)

        return alunos_dict

    def get_all_alunos(self) -> dict:
        """Retrieves all existing Aluno objects from the repository.
        Returns a dictionary of alunos, where every aluno object is a
        dictionary itself.\\
        Returns:
            alunos_dict (dict): A dictionary of alunos.
        """
        alunos = self.aluno_repository.get_all_alunos()

        # get all alunos and change it to a dictionary of alunos
        alunos_dict = {'Aluno': []}
        for aluno in alunos:
            alunos_dict['Aluno'].append(aluno.__dict__)

        return alunos_dict

    def get_alunos_paginated(self, offset, limit, name_like):
        """Retrieves a paginated list of existing Aluno objects from the
        repository. Returns a dictionary of alunos, where every aluno object
        is a dictionary itself.\\
        Args:
            offset (int): The offset of the query.
            limit (int): The limit of the query.
            name_like (str): A string to be used in the query to search for
                alunos with a similar name.
        Returns:
            alunos_dict (dict): A dictionary of alunos.
        """
        alunos = self.aluno_repository.get_alunos_paginated(offset, limit, name_like)

        # get all alunos and change it to a dictionary of alunos
        alunos_dict = {'Aluno': []}
        if alunos is not None:
            for aluno in alunos:
                alunos_dict['Aluno'].append(aluno.__dict__)

        return alunos_dict
