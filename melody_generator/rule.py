from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Rule:
    left_symbol: str
    right_symbols: tuple[str, ...]
