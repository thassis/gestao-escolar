"""Database repositories module.

- Implementa as operações necessárias para o domínio salvar os dados de Aluno
- Implementa a interface para salvar e recuperar dados de PRofessor do DB
- Aqui, pode ser usado qualquer tecnologia
"""

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import column

from backend.core.domain.models.Aluno import Aluno
from backend.core.interfaces.repositories.AlunoRepository import AlunoRepository

from backend.adapters.database.ORMs.AlunoORM import AlunoORM

class AlunoRepositoryPostgres(AlunoRepository):
    """Aluno repository class for PostgreSQL implementation."""

    def __init__(self, db: Session):
        """Initializes the repository with a database session."""
        self.database = db


    def save(self, aluno: Aluno) -> Aluno | str:
        """Saves an Aluno object to the database. If the save fails,
        an exception is raised and the error message is returned.\\
        Args:
            aluno (Aluno): Aluno object to be saved.
        Returns:
            Aluno | str: Aluno object if the save is successful. Otherwise,
                returns an error message.
        """
        try:
            aluno_orm = AlunoORM.from_aluno(aluno)
            self.database.add(aluno_orm)
            self.database.commit()
            self.database.refresh(aluno_orm)
        except SQLAlchemyError as exception:
            error_message = f"An error occurred: {exception}"
            print(error_message) # TODO: Remove later
            return error_message
        return aluno


    def get_by_id(self, aluno_id: int) -> Aluno | str:
        """Retrieves an Aluno object from the database by its ID. If the
        retrieval fails, an error message is returned.\\
        Args:
            aluno_id (int): Aluno's ID.
        Returns:
            Aluno | str: Aluno object if the retrieval is successful. Otherwise,
                returns an error message.
        """
        aluno = self.database.query(AlunoORM).filter_by(id=aluno_id).first()
        if aluno is None:
            return f"Aluno with ID {aluno_id} not found"
        return aluno


    def delete(self, aluno: Aluno) -> str:
        """Deletes an Aluno object from the database. If the deletion fails,
        an exception is raised and the error message is returned.\\
        Args:
            aluno (Aluno): Aluno object to be deleted.
        Returns:
            str: Error message if the deletion fails. Otherwise,
                returns a success message.
        """
        try:
            self.database.delete(aluno)
            self.database.commit()
        except SQLAlchemyError as exception:
            error_message = f"An error occurred: {exception}"
            print(error_message) # TODO: Remove later
            return error_message
        return "Removed successfully"


    def get_by_name(self, aluno_name: str) -> list[Aluno]:
        """Retrieves one or more Aluno object from the database by its name.\\
        Args:
            aluno_name (str): Aluno name.
        Returns:
            list[Aluno]: List of Aluno objects.
        """
        alunos = self.database.query(AlunoORM).filter(column('name') == aluno_name).all()
        alunos = [AlunoORM.to_aluno(aluno) for aluno in alunos]
        if alunos is None:
            return []
        return alunos


    def get_all_alunos(self) -> list[Aluno]:
        """Retrieves all Aluno objects from the database. If the retrieval
        fails, an empty list is returned.\\
        Returns:
            list[Aluno]: List of Aluno objects.
        """
        alunos_orm = self.database.query(AlunoORM).all()
        alunos = [AlunoORM.to_aluno(aluno) for aluno in alunos_orm]
        if alunos is None:
            return []
        return alunos


    def get_alunos_paginated(self, offset, limit, name_like) -> list[Aluno]:
        """Retrieves all Aluno objects from the database. If the retrieval
        fails, an empty list is returned.\\
        Returns:
            list[Aluno]: List of Aluno objects.
        """
        alunos_orm = self.database.query(
                         AlunoORM).filter(
                         AlunoORM.name.like(f'%{name_like}%')
                         ).offset(offset).limit(limit).all()

        alunos = [AlunoORM.to_aluno(aluno) for aluno in alunos_orm]
        if alunos is None:
            return []
        return alunos