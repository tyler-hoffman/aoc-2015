class Parser(object):
    @staticmethod
    def parse(input: str) -> set[int]:
        lines = input.strip().splitlines()
        return {int(line) for line in lines}
