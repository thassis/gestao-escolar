"""Database ORM models for SQLAlchemy."""

from sqlalchemy import create_engine, Engine
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship


class DatabaseSession:
    """Database session class for SQLAlchemy. It creates a database engine
    and a session. The engine is used to create the database tables and
    the session is used to query the database. The engine and session
    are passed to the repositories.\\
    """
    def __init__(self):
        """Initializes the database engine and session."""
        # postgresql://<username>:<password>@<host>:<port>/<database_name>
        self.engine = create_engine(
            'postgresql://postgres:postgres@172.18.0.2:5432/postgres',
            echo=True)

        self.db_session = Session(bind=self.engine)

    def get_db_session(self) -> Session:
        """Returns the SQLAlchemy session."""
        return self.db_session

    def close_db_session(self):
        """Closes the database session."""
        self.db_session.close()

    def get_engine(self) -> Engine:
        """Returns the SQLAlchemy engine."""
        return self.engine


Base = declarative_base()

class AlunoORM(Base):
    """Aluno ORM class for SQLAlchemy."""
    __tablename__ = 'aluno'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    born_date = Column(Date, nullable=False)
    address = Column(String(200), nullable=False)
    tutor_name = Column(String(100), nullable=False)
    tutor_phone = Column(String(20), nullable=False)
    class_shift = Column(String(20), nullable=False)


class ProfessorORM(Base):
    """Professor ORM class for SQLAlchemy."""
    __tablename__ = 'professor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)


class PeriodoLetivoORM(Base):
    """PeriodoLetivo ORM class for SQLAlchemy."""
    __tablename__ = 'periodo_letivo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    class_shift = Column(String(100), nullable=False)
    dias_sem_aula = relationship("DiaSemAulaORM", backref="periodo_letivo")


class DiaSemAulaORM(Base):
    """DiaSemAula ORM class for SQLAlchemy."""
    __tablename__ = 'dia_sem_aula'

    id = Column(Integer, primary_key=True, autoincrement=True)
    periodo_letivo_id = Column(Integer, ForeignKey('periodo_letivo.id'), nullable=False)
    date = Column(Date, nullable=False)
    reason = Column(String(100), nullable=False)


def create_tables(engine: Engine):
    """Creates the database tables."""
    Base.metadata.create_all(engine)


def create_some_alunos(engine: Engine):
    """Creates some Aluno objects and saves them to the database."""
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    new_aluno = AlunoORM(name='John Doe', born_date='2000-01-01',
                         address='123 Main St', tutor_name='Jane Doe',
                         tutor_phone='555-555-5555', class_shift='Morning')
    session.add(new_aluno)
    session.commit()

    # Insert a new student with a different class shift
    new_aluno = AlunoORM(name='Jane Doe', born_date='2001-02-02',
                         address='456 Elm St', tutor_name='John Doe',
                         tutor_phone='555-555-5555', class_shift='Afternoon')
    session.add(new_aluno)
    session.commit()

    # Insert a new student with a different tutor
    new_aluno = AlunoORM(name='Bob Smith', born_date='2002-03-03',
                         address='789 Oak St', tutor_name='Alice Smith',
                         tutor_phone='555-555-5555', class_shift='Morning')
    session.add(new_aluno)
    session.commit()

    # Insert a new student with a different address
    new_aluno = AlunoORM(name='Samantha Johnson', born_date='2003-04-04',
                         address='321 Pine St', tutor_name='Mike Johnson',
                         tutor_phone='555-555-5555', class_shift='Afternoon')
    session.add(new_aluno)
    session.commit()


def create_a_professor(engine: Engine):
    """Creates a Professor object and saves it to the database."""
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    # Insert a new professor
    new_professor = ProfessorORM(name='Oscar Smith',
                                 email='oscar.smith@example.com',
                                 password='password123')
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

    new_periodo_letivo = PeriodoLetivoORM(start_date='2023-01-01',
                                          end_date='2023-06-30',
                                          class_shift='Morning')
    session.add(new_periodo_letivo)
    session.commit()

    # Insert a new periodo letivo with a different class shift
    new_periodo_letivo = PeriodoLetivoORM(start_date='2023-01-01',
                                          end_date='2023-06-30',
                                          class_shift='Afternoon')
    session.add(new_periodo_letivo)
    session.commit()


def create_some_dias_sem_aula(engine: Engine):
    """Creates some DiaSemAula objects and saves them to the database."""
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    new_dia_sem_aula = DiaSemAulaORM(periodo_letivo_id=1,
                                     date='2023-01-01',
                                     reason='Feriado')
    session.add(new_dia_sem_aula)
    session.commit()

    # Insert a new dia sem aula with a different reason
    new_dia_sem_aula = DiaSemAulaORM(periodo_letivo_id=1,
                                     date='2023-01-02',
                                     reason='Feriado')
    session.add(new_dia_sem_aula)
    session.commit()

    # Insert a new dia sem aula with a different date
    new_dia_sem_aula = DiaSemAulaORM(periodo_letivo_id=1,
                                     date='2023-01-03',
                                     reason='Feriado')
    session.add(new_dia_sem_aula)
    session.commit()

    # Insert a new dia sem aula with a different periodo letivo
    new_dia_sem_aula = DiaSemAulaORM(periodo_letivo_id=2,
                                     date='2023-01-01',
                                     reason='Feriado')
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
