
def boxBlur(image):
    offset = (0, 1, -1)
    indices = [(i, j) for i in offset for j in offset]
    result = []
    # tmp = 0
    # print(indices)column
    for x, row in enumerate(image[1:-1], 1):
        # print(x, row)
        result.append([])
        for y, _ in enumerate(row[1:-1], 1):
            tmp = 0
            for pos in indices:
                row = x + pos[0]
                col = y + pos[1]
                # print(f"{x}, {y} ---->  {image[row][col]}")

                tmp += image[row][col]

            result[-1].append(round((tmp//9)))

    return result


image = [[1, 1, 1],
         [1, 7, 1],
         [1, 1, 1]]

print(boxBlur(image))

image = [[7, 4, 0, 1],
         [5, 6, 2, 2],
         [6, 10, 7, 8],
         [1, 4, 2, 0]]


print(boxBlur(image))
# =[[1]])
