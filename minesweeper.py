def minesweeper(matrix):
    offset = (0, 1, -1)
    bombs = [(x, y) for x, row in enumerate(matrix) for y, item in enumerate(row) if item]
    matrix = [[0 for x in row] for row in matrix]
    for bomb in bombs:
        row, column = bomb
        indices = [(row + x, column + y) for x in offset if 0 <= row + x <= len(matrix)-1 for y in offset if 0 <= column + y <= len(matrix[0])-1]
        for pos in indices[1:]:
            x, y = pos
            matrix[x][y] += 1
    return matrix




matrix = [[True, False, False, True],
          [False, False, True, False],
          [True, True, False, True]]


print(minesweeper(matrix))

# [[0, 2, 2, 1],
#  [3, 4, 3, 3],
#  [1, 2, 3, 1]]
