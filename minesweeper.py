def minesweeper(matrix):
    offset = (0, 1, -1)
    # indices = [(i, j) for i in offset for j in offset]
    bombs = [(x, y) for x, row in enumerate(matrix) for y, item in enumerate(row) if item]
    matrix = [["b" if x else 0 for x in row] for row in matrix]
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == "b":
                matrix[row][column]
                indices = [(row + x, column + y) for x in offset if 0 <= row + x <= len(matrix)-1 for y in offset if 0 <= column + y <= len(matrix[0])-1]
                # print(row, column)
                # print(indices[1:])

                for pos in indices[1:]:
                    # print(pos)
                    x, y = pos
                    if matrix[x][y] != "b":
                        matrix[x][y] += 1

    return [[1 if x == "b" else x for x in row] for row in matrix]


matrix = [[True, False, False, True],
          [False, False, True, False],
          [True, True, False, True]]


print(minesweeper(matrix))

# [[0, 2, 2, 1],
#  [3, 4, 3, 3],
#  [1, 2, 3, 1]]
