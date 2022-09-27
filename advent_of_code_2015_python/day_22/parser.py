from advent_of_code_2015_python.day_22.shared import Enemy


class Parser(object):
    @staticmethod
    def parse(input: str) -> Enemy:
        lines = input.strip().splitlines()
        amount_strings = [line.split()[-1] for line in lines]
        amounts = [int(x) for x in amount_strings]
        hp, dmg = amounts
        return Enemy(hp=hp, dmg=dmg)
