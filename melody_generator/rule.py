"""Модуль для работы с порождающими правилами стохастической L-системы."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Rule:
    """Порождающее правило стохастической L-системы."""

    left_symbol: str
    right_symbols: tuple[str, ...]
