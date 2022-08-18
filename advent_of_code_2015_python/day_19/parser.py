from dataclasses import replace
from typing import Optional

from advent_of_code_2015_python.day_19.shared import Replacement


class Parser(object):
    @staticmethod
    def parse(input: str) -> tuple[str, set[Replacement]]:
        replacements: set[Replacement] = set()
        molecule: Optional[str]
        checking_replacements = True
        lines = input.strip().splitlines()

        for line in lines:
            if not line:
                checking_replacements = False
            elif checking_replacements:
                original, replacement = line.split(" => ")
                replacements.add(Replacement(original, replacement))
            else:
                molecule = line

        assert molecule is not None
        return molecule, replacements
