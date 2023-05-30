"""Domain models for the school management system. It follows hexagonal
architecture principles."""

from dataclasses import dataclass
from datetime import date

@dataclass
class Presenca:
    """Presenca model class for domain layer."""
    id: int | None
    aluno_id: int
    status: str
    document: str
    reason_missing_class: str