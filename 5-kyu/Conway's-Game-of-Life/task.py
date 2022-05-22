def sum_around(cells, i, j):
    return cells[i][j - 1] + cells[i][j + 1] + sum(cells[i - 1][j - 1:j + 2]) + sum(cells[i + 1][j - 1:j + 2])


def next_gen(cells):
    N = len(cells)
    M = len(cells[0])

    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    cells = [[cells[i - 1][j - 1] if i not in (0, N + 1) and j not in (0, M + 1) else 0 for j in range(M + 2)] for i in
             range(N + 2)]

    new_cells = [[0 for j in range(M)] for i in range(N)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            around = sum_around(cells, i, j)
            # Any live cell with fewer than two live neighbours dies, as if caused by under-population.
            if cells[i][j] == 0 and around < 2:
                new_cells[i - 1][j - 1] = 0
            # Any live cell with two or three live neighbours lives on to the next generation.
            elif cells[i][j] == 1 and 2 <= around <= 3:
                new_cells[i - 1][j - 1] = 1
            # Any live cell with more than three live neighbours dies, as if by overcrowding.
            elif cells[i][j] == 1 and around > 3:
                new_cells[i - 1][j - 1] = 0
            # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            elif cells[i][j] == 0 and around == 3:
                new_cells[i - 1][j - 1] = 1

    return new_cells


new_cells = next_gen([
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
])

for i in range(len(new_cells)):
    for j in range(len(new_cells[0])):
        print(new_cells[i][j], end=" ")
    print()
