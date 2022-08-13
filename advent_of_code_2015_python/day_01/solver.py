from abc import ABC
from dataclasses import dataclass
from typing import Sequence


@dataclass
class Solver(ABC):
    input: Sequence[str]
