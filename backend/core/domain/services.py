"""Domain layer services module."""

from backend.core.domain.models import Aluno


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
