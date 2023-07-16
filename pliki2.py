# Rozwiązanie od Macieja
def read_n_lines(n: int, file: str) -> str:
    with open(file, "r") as f:
        lines = [f.readline() for _ in range(n)]

    return "".join(lines)