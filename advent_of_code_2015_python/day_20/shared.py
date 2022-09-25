from dataclasses import dataclass
from functools import cache, cached_property
from math import ceil, sqrt

from advent_of_code_2015_python.shared.optimus import Optimus


@dataclass(frozen=True)
class DivisorCalculator:
    @cache
    def divisors(self, n: int) -> set[int]:
        output: set[int] = {1, n}

        prime_cap = ceil(sqrt(n))
        primes = self.optimus.get_primes_up_to(prime_cap)

        for p in primes:
            if n % p == 0:
                q = n // p
                b_divisors = self.divisors(q)

                output.add(p)
                output.add(q)
                output.update(b_divisors)
                output.update({p * x for x in b_divisors})
                break

        return output

    @cached_property
    def optimus(self) -> Optimus:
        return Optimus()
