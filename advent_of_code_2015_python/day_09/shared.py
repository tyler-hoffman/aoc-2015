from dataclasses import dataclass


@dataclass(frozen=True)
class Segment:
    a: str
    b: str
    distance: int
