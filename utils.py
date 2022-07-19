def _get_test_input_info(filename) -> tuple[int, list[int]]:
    with open(f"input/{filename}") as f:
        readline = lambda f: int(f.readline().strip())

        n = readline(f)
        w = readline(f)

        itens = []

        for _ in range(n):
            item = readline(f)
            itens.append(item)

    return (w, itens)


def get_problem_info(problem: str) -> tuple[int, int, list[int]]:
    with open("optimal-solution/solutions.csv") as f:
        text = f.read()

        for line in text.splitlines():
            if line.startswith(problem):
                filename, optimal_solution = line.split(",")
                optimal_solution = int(optimal_solution.strip())

                w, itens = _get_test_input_info(filename)

                return (optimal_solution, w, itens)