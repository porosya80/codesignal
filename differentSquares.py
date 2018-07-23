def differentSquares(matrix):
    mat2 = set()
    for r, row in enumerate( matrix[:-1]):
        for c, col in enumerate(row[:-1]):
            mat2.add((matrix[r][c], matrix[r][c+1], matrix[r+1][c], matrix[r+1][c+1]))

    # print(mat2)
    return len(mat2)




matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]


print(differentSquares(matrix))
# 6
