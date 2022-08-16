from dataclasses import dataclass


@dataclass
class Solver:
    input_str: str
    iterations: int = 40

    @property
    def solution(self) -> int:
        string = self.input_str
        for _ in range(self.iterations):
            string = self.next(string)
        return len(string)

    @staticmethod
    def next(string: str) -> str:
        output_array: list[str] = []
        current_char: str = string[0]
        count = 1
        for char in string[1:]:
            if char != current_char:
                output_array.append(str(count))
                output_array.append(current_char)
                current_char = char
                count = 1
            else:
                count += 1
        output_array.append(str(count))
        output_array.append(current_char)

        return "".join([str(x) for x in output_array])
