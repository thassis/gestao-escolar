from adapters.database.database import (
    DatabaseSession, create_tables, create_some_alunos, create_a_professor,
    delete_all_alunos, delete_all_professors
)


database_session = DatabaseSession()
engine = database_session.get_engine()

create_tables(engine)

create_some_alunos(engine)
create_a_professor(engine)

# delete_all_alunos(engine)
# delete_all_professors(engine)
