"""Domain models for the school management system. It follows hexagonal
architecture principles."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Aluno:
    """Aluno model class for domain layer."""
    id: int | None
    name: str
    born_date: date
    address: str
    tutor_name: str
    tutor_phone: str
    class_shift: str