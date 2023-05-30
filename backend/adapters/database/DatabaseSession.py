"""Database ORM models for SQLAlchemy."""

from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

import sys
sys.path.append('../../../')

Base = declarative_base()

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
            'postgresql://postgres:postgres@172.19.0.2:5432/postgres',
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
