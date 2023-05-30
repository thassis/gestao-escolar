"""Database repositories module.

- Implementa as operações necessárias para o domínio salvar os dados de Professor
- Implementa a interface para salvar e recuperar dados de PRofessor do DB
- Aqui, pode ser usado qualquer tecnologia
"""

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import column

from backend.core.domain.models.Professor import Professor
from backend.core.interfaces.repositories.ProfessorRepository import ProfessorRepository

from backend.adapters.database.ORMs.ProfessorORM import ProfessorORM

class ProfessorRepositoryPostgres(ProfessorRepository):
    """Professor repository class for PostgreSQL implementation."""

    def __init__(self, db: Session):
        """Initializes the repository with a database session."""
        self.database = db


    def verify_login(self, professor_email: str, professor_password: str) -> bool | str:
        """Verifies professor login credentials. It queries the database for
        a professor with the given email and checks if the password matches.\\
        Args:
            email (str): Professor's email.
            password (str): Professor's password.
        Returns:
            bool | str: True if the credentials are valid. False if the
                credentials are invalid. Otherwise, returns an error message.
        """
        try:
            professor_object = self.database.query(ProfessorORM).filter_by(email=professor_email).first()
        except SQLAlchemyError as exception:
            error_message = f"An error occurred: {exception}"
            print(error_message)
            return error_message
        if professor_object is None:
            return False

        return professor_object.password == professor_password


    def save(self, professor: Professor) -> Professor | str:
        """Saves a Professor object to the database. If the save fails,
        an exception is raised and the error message is returned.\\
        Args:
            professor (Professor): Professor object to be saved.
        Returns:
            Professor | str: Professor object if the save is successful.
                Otherwise, returns an error message.
        """
        try:
            professor_orm = ProfessorORM.from_professor(professor)
            self.database.add(professor_orm)
            self.database.commit()
            self.database.refresh(professor_orm)
        except SQLAlchemyError as exception:
            error_message = f"An error occurred: {exception}"
            print(error_message) # TODO: Remove later
            return error_message
        return professor


    def delete(self, professor: Professor) -> str:
        """Deletes a Professor object from the database.  If the deletion fails,
        an exception is raised and the error message is returned.\\
        Args:
            professor (Professor): Professor object to be deleted.
        Returns:
            str: Error message if the deletion fails. Otherwise,
                returns a success message.
        """
        try:
            self.database.delete(professor)
            self.database.commit()
        except SQLAlchemyError as exception:
            error_message = f"An error occurred: {exception}"
            print(error_message) # TODO: Remove later
            return error_message
        return "Removed successfully"


    def get_by_id(self, professor_id: int) -> Professor | str:
        """Retrieves a Professor object from the database by its ID. If the
        retrieval fails, an error message is returned.\\
        Args:
            professor_id (int): Professor's ID.
        Returns:
            Professor | str: Professor object if the retrieval is successful.
                Otherwise, returns an error message.
        """
        professor = self.database.query(Professor).filter_by(id=professor_id).first()
        if professor is None:
            return f"Professor with ID {professor_id} not found"
        return professor


    def get_by_name(self, professor_name: str) -> list[Professor]:
        """Retrieves one or more Professor object from the database by its name.\\
        Args:
            professor_name (str): Professor name.
        Returns:
            list[Professor]: List of Professor objects.
        """
        professors = self.database.query(Professor).filter(column('name') == professor_name).all()
        if professors is None:
            return []
        return professors