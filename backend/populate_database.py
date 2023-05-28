"""Populate the database with some data."""

from adapters.database.database import (
    DatabaseSession, create_tables, create_some_alunos, create_some_professor,
    create_some_periodos_letivos, create_some_dias_sem_aula
    delete_all_alunos, delete_all_professors
)


database_session = DatabaseSession()
engine = database_session.get_engine()

create_tables(engine)

create_some_alunos(engine)
create_some_professor(engine)
create_some_periodos_letivos(engine)
create_some_dias_sem_aula(engine)
# delete_all_alunos(engine)
# delete_all_professors(engine)
