"""Functions to populate Database to test aplication"""

from sqlalchemy import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from backend.adapters.database.ORMs.AlunoORM import AlunoORM
from backend.adapters.database.ORMs.ProfessorORM import ProfessorORM
from backend.adapters.database.ORMs.PeriodoLetivoORM import PeriodoLetivoORM
from backend.adapters.database.ORMs.DiasSemAulaORM import DiaSemAulaORM
import sys
sys.path.append('../../../')

Base = declarative_base()

def create_tables(engine: Engine):
    """Creates the database tables."""
    Base.metadata.create_all(engine)


def create_some_alunos(engine: Engine):
    """Creates some Aluno objects and saves them to the database."""
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    aluno_list = [
        {'name': 'João Silva', 'born_date': '2000-01-01',
         'address': 'Rua Principal, 123', 'tutor_name': 'Maria Silva',
         'tutor_phone': '(11) 5555-5555', 'class_shift': 'Manhã'},
        {'name': 'Maria Silva', 'born_date': '2001-02-02',
         'address': 'Rua das Flores, 456', 'tutor_name': 'João Silva',
         'tutor_phone': '(11) 5555-5555', 'class_shift': 'Tarde'},
        {'name': 'Roberto Santos', 'born_date': '2002-03-03',
         'address': 'Rua dos Pinheiros, 789', 'tutor_name': 'Alice Santos',
         'tutor_phone': '(11) 5555-5555', 'class_shift': 'Manhã'},
        {'name': 'Samantha Oliveira', 'born_date': '2003-04-04',
         'address': 'Rua das Palmeiras, 321', 'tutor_name': 'Miguel Oliveira',
         'tutor_phone': '(11) 5555-5555', 'class_shift': 'Tarde'}
    ]

    for aluno in aluno_list:
        new_aluno = AlunoORM(name=aluno['name'], born_date=aluno['born_date'],
                             address=aluno['address'], tutor_name=aluno['tutor_name'],
                             tutor_phone=aluno['tutor_phone'], class_shift=aluno['class_shift'])

        existing_aluno = session.query(AlunoORM).filter_by(name=new_aluno.name, born_date=new_aluno.born_date).first()
        if existing_aluno: # avoid duplicates and errors for existing data
            continue

        # Insert a new student
        session.add(new_aluno)
        session.commit()


def create_some_professor(engine: Engine):
    """Creates some Professor objects and saves it to the database."""
    session_maker = sessionmaker(bind=engine)
    session = session_maker()
    professor_list = [
        {'name': 'William', 'email': 'william@bhzconnection.org.br',
        'password': 'password123'}
    ]
    for professor in professor_list:
        new_professor = ProfessorORM(name=professor['name'],
                                     email=professor['email'],
                                     password=professor['password'])

        existing_professor = session.query(ProfessorORM).filter_by(email=new_professor.email).first()
        if existing_professor: # avoid duplicates and errors for existing data
            continue

        # Insert a new professor
        session.add(new_professor)
        session.commit()

def delete_all_alunos(engine: Engine):
    """Deletes all Aluno objects from the database."""
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    # Delete all alunos
    session.query(AlunoORM).delete()
    session.commit()


def delete_all_professors(engine: Engine):
    """Deletes all Professor objects from the database."""
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    # Delete all professors
    session.query(ProfessorORM).delete()
    session.commit()


def create_some_periodos_letivos(engine: Engine):
    """Creates some PeriodoLetivo objects and saves them to the database."""
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    periodo_letivo_list = [
        {'start_date': '2023-01-01', 'end_date': '2023-06-30', 'class_shift': 'Manhã'},
    ]

    for periodo_letivo in periodo_letivo_list:
        new_periodo_letivo = PeriodoLetivoORM(start_date=periodo_letivo['start_date'],
                                              end_date=periodo_letivo['end_date'],
                                              class_shift=periodo_letivo['class_shift'])

        existing_periodo_letivo = session.query(PeriodoLetivoORM).filter_by(start_date=new_periodo_letivo.start_date, end_date=new_periodo_letivo.end_date).first()
        if existing_periodo_letivo: # avoid duplicates and errors for existing data
            continue

        # Insert a new periodo letivo
        session.add(new_periodo_letivo)
        session.commit()


def create_some_dias_sem_aula(engine: Engine):
    """Creates some DiaSemAula objects and saves them to the database."""
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    dia_sem_aula_list = [
        {'periodo_letivo_id': 1, 'date': '2023-01-01', 'reason': 'Feriado'},
        {'periodo_letivo_id': 1, 'date': '2023-01-02', 'reason': 'Feriado'},
        {'periodo_letivo_id': 1, 'date': '2023-01-03', 'reason': 'Feriado'},
    ]

    for dia_sem_aula in dia_sem_aula_list:
        new_dia_sem_aula = DiaSemAulaORM(periodo_letivo_id=dia_sem_aula['periodo_letivo_id'],
                                        date=dia_sem_aula['date'],
                                        reason=dia_sem_aula['reason'])

        existing_dia_sem_aula = session.query(DiaSemAulaORM).filter_by(periodo_letivo_id=new_dia_sem_aula.periodo_letivo_id, date=new_dia_sem_aula.date, reason=new_dia_sem_aula.reason).first()
        if existing_dia_sem_aula: # avoid duplicates and errors for existing data
            continue

        # Insert a new dia sem aula
        session.add(new_dia_sem_aula)
        session.commit()


def delete_all_periodos_letivos(engine: Engine):
    """Deletes all PeriodoLetivo objects from the database."""
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    # Delete all periodos letivos
    session.query(PeriodoLetivoORM).delete()
    session.commit()

def delete_all_dias_sem_aula(engine: Engine):
    """Deletes all DiaSemAula objects from the database."""
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    # Delete all dias sem aula
    session.query(DiaSemAulaORM).delete()
    session.commit()
