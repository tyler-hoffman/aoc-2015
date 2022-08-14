import hashlib
from dataclasses import dataclass


@dataclass
class Solver:
    secret: str
    prefix: str

    @property
    def solution(self) -> int:
        x = 1
        while True:
            to_try = f"{self.secret}{x}"
            hashed = hashlib.md5(to_try.encode("utf-8"))
            hex = hashed.hexdigest()
            if hex.startswith(self.prefix):
                return x
            x += 1
