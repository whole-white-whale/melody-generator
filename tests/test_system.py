from melody_generator.rule import Rule
from melody_generator.system import System


class TestSystem:
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
