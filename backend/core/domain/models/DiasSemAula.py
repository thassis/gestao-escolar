"""Domain models for the school management system. It follows hexagonal
architecture principles."""

from dataclasses import dataclass
from datetime import date

@dataclass
class DiaSemAula:
    """DiaSemAula model class for domain layer."""
    id: int | None
    periodo_letivo_id: int
    date: date
    reason: str