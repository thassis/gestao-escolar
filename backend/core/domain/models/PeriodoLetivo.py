"""Domain models for the school management system. It follows hexagonal
architecture principles."""

from dataclasses import dataclass
from datetime import date

@dataclass
class PeriodoLetivo:
    """PeriodoLetivo model class for domain layer."""
    id: int | None
    start_date: date
    end_date: date
    class_shift: str