"""Domain layer services module.

- O serviço está desacoplado de qualquer implementação específica,
  tal como DB ou ORM
"""

from backend.core.domain.models import Aluno


class ProfessorService:
    """Professor service class for domain layer. It provides methods for
    verifying professor login credentials. It takes a professor_repository
    object as a dependency."""

    def __init__(self, professor_repository):
        """Initializes the service with a ProfessorRepository object."""
        self.professor_repository = professor_repository

    def verify_login(self, email, password):
        """Verifies professor login credentials."""
        login = self.professor_repository.verify_login(email, password)
        if login is None:
            return False
        return login


class AlunoService:
    """Aluno service class for domain layer. It provides methods for
    creating, updating, and removing Aluno objects. It takes an
    aluno_repository object as a dependency."""

    def __init__(self, aluno_repository):
        """Initializes the service with an AlunoRepository object."""
        self.aluno_repository = aluno_repository

    def create_aluno(self, name, born_date, address, tutor_name,
                    tutor_phone, class_shift):
        """Creates a new Aluno object and saves it to the repository."""
        aluno = Aluno(
            id=None, # BUG
            name=name,
            born_date=born_date,
            address=address,
            tutor_name=tutor_name,
            tutor_phone=tutor_phone,
            class_shift=class_shift
        )
        self.aluno_repository.save(aluno)
        return aluno


    def update_aluno(self, aluno_id, name=None, born_date=None,
                        address=None, tutor_name=None, tutor_phone=None,
                        class_shift=None):
        """Updates an existing Aluno object and saves it to the repository."""
        aluno = self.aluno_repository.get_by_id(aluno_id)
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
        self.aluno_repository.delete(aluno)


    def get_alunos_by_name(self, aluno_name: str) -> dict:
        """Retrieves one or more existing Aluno object from the repository.
        Returns a dictionary of alunos, where every aluno object is a

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
