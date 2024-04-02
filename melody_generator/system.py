"""Модуль для работы со стохастической L-системой."""

import random

from dataclasses import dataclass
from typing import Generator, Sequence

from melody_generator.rule import Rule


@dataclass(frozen=True, slots=True)
class System:
    """Стохастическая L-система."""

    symbols: set[str]
    start_symbol: str
    rules: set[Rule]

    @classmethod
    def from_configuration(cls, configuration: Sequence[str], start_symbol="1"):
        """Построить стохастическую L-систему, соответствующую данной конфигурации."""

        symbols, rules = set(), set()

        for line in configuration:
            left, _, right = line.partition("->")

            left_symbol, right_symbols = left.strip(), tuple(
                symbol for symbol in right if not symbol.isspace()
            )

            symbols.add(left_symbol)

            for symbol in right_symbols:
                symbols.add(symbol)

            rules.add(Rule(left_symbol, right_symbols))

        return System(symbols, start_symbol, rules)

    def get_rules_with_left_symbol(self, symbol: str) -> set[Rule]:
        """Получить порождающие правила с данным символом в левой части."""

        return {rule for rule in self.rules if rule.left_symbol == symbol}

    def get_random_rule_with_left_symbol(self, symbol: str) -> Rule:
        """Получить случайное порождающее правило с данным символом в левой части."""

        return random.choice(list(self.get_rules_with_left_symbol(symbol)))

    def get_random_rule_table(self) -> dict[str, Rule]:
        """Получить случайную таблицу порождающих правил для каждого символа."""

        return {
            symbol: self.get_random_rule_with_left_symbol(symbol)
            for symbol in self.symbols
        }

    def produce(self) -> Generator[list[str], None, None]:
        """Породить очередную последовательность символов."""

        symbols = [self.start_symbol]

        while True:
            yield symbols

            rule_table, new_symbols = self.get_random_rule_table(), []

            for symbol in symbols:
                rule = rule_table[symbol]
                new_symbols.extend(rule.right_symbols)

            symbols = new_symbols
