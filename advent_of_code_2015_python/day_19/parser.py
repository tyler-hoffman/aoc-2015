from dataclasses import replace
from typing import Optional

from advent_of_code_2015_python.day_19.shared import StrReplacement


class Parser(object):
    @staticmethod
    def parse(input: str) -> tuple[str, set[StrReplacement]]:
        replacements: set[StrReplacement] = set()
        molecule: Optional[str]
        checking_replacements = True
        lines = input.strip().splitlines()

        for line in lines:
            if not line:
                checking_replacements = False
            elif checking_replacements:
                original, replacement = line.split(" => ")
                replacements.add(StrReplacement(original, replacement))
            else:
                molecule = line

        assert molecule is not None
        return molecule, replacements
