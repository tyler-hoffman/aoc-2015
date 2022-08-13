def create_solver_stub() -> str:
    return _SOLVER_TEMPLATE


_SOLVER_TEMPLATE = """
from abc import ABC
from dataclasses import dataclass


@dataclass
class Solver(ABC):
    ...

"""
