def chessKnight(cell):
    x, y = ord(cell[0]) % 32, int(cell[1])
    moves = [(x1, y1) for x1 in (-2, -1, 1, 2) for y1 in (-2, -1, 1, 2) if abs(x1) != abs(y1) and 0 < x+x1 < 9 and 0 < y+y1 < 9]
    return len(moves)


cell = "d5"
print(chessKnight(cell))
# _ = 2
