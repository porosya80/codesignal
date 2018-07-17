def bishopAndPawn(bishop, pawn):
    x, y = ord(bishop[0]) % 32, int(bishop[1])
    x1, y1 = ord(pawn[0]) % 32, int(pawn[1])

    return True if abs(x-x1) == abs(y-y1) else False


bishop = "h1"
pawn = "h3"
print(bishopAndPawn(bishop, pawn))
