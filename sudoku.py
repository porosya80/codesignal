def sudoku(grid):
    moves = [(x, y) for x in [1, 0, -1] for y in [1, 0, -1]]
    etal = set(range(1, 10))
    # check = []
    for row in grid:
        if set(row) != etal:
            return False
    for row in zip(*list(grid)):
        if set(row) != etal:
            return False
    for row in range(1, 9, 3):
        for col in range(1, 9, 3):
            check = []
            for x, y in moves:
                check.append(grid[row+x][col+y])
                # print(grid[row][col])

            if set(check) != etal:

                return False
    return True


grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]]

print(sudoku(grid))
# True
