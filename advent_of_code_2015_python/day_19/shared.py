from dataclasses import dataclass


@dataclass(frozen=True)
class Replacement:
    original: str
    replacement: str

    def __repr__(self) -> str:
        return f"{self.original} => {self.replacement}"
