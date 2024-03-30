from melody_generator.rule import Rule
from melody_generator.system import System


class TestSystem:
    def test_from_configuration(self):
        system = System.from_configuration(
            [
                "1 ->",
                "2 -> 2",
                "3 -> 4 5",
                "6 -> 7 8 9",
            ]
        )

        have = system.symbols

        want = {
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        }

        assert have == want

    def test_produce(self):
        symbols = {"s", "t"}

        rules = {
            Rule("s", ("t", "t")),
            Rule("t", ("s", "s")),
        }

        system = System(symbols, "s", rules)

        want = [
            ["s"],
            ["t", "t"],
            ["s", "s", "s", "s"],
        ]

        have = []

        for _, symbols in zip(range(3), system.produce()):
            have.append(symbols)

        assert have == want
