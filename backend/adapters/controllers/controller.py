from backend.core.domain.services import AlunoService, ProfessorService
from backend.adapters.database.repositories import AlunoRepositoryPostgres


class AlunoController:
    def __init__(self) -> None:
        self.aluno_repository = None # AlunoRepositoryPostgres
        self.db = None # instanciar db
        self.alunoService = None # instanciar aluno service


    def get_alunos_by_name(self, name):
        #return self.alunoService.get_alunos_by_name(name)
        return True


    def create(self, name, born_date, address, tutor_name,
                    tutor_phone, class_shift):
        #return self.alunoService.create_aluno(name, born_date, address, tutor_name,
        #            tutor_phone, class_shift)
        return True

    def update(self, aluno_id, name=None, born_date=None,
                        address=None, tutor_name=None, tutor_phone=None,
                        class_shift=None):
        #return self.alunoService.update_aluno(aluno_id, name, born_date,
        #                address, tutor_name, tutor_phone,
        #                class_shift)
        return True

    def remove(self, aluno_id):
        #return self.alunoService.remove_aluno(aluno_id)
        return True

class ProfessorController:
    def __init__(self,) -> None:
        self.professor_repository = None #ProfessorRepositoryPostgres
        self.db = None # instanciar db
        self.professorService = None # instanciar professor service

    def login(self, email, password) -> tuple:
        print(email, password)
        #self.professorService.verify_login(email, password)
        return True

    def create(self, name, email, password):
        #return self.professorService.create_professor(name, email, password)
        return True

    def update(self, professor_id, name=None, email=None,
                        password=None):
        #return self.professorService.update_professor(professor_id, name, email, password)
        return True

    def remove(self, professor_id):
        #return self.professorService.delete_professor(professor_id)
        return True
