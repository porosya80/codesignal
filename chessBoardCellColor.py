def chessBoardCellColor(cell1, cell2):
    board = 'abcdefgh'.upper()
    return (board.index(cell1[0])+1+int(cell1[1]))%2 == (board.index(cell2[0])+1+int(cell2[1]))%2


cell1 = "A1"
cell2 = "C3"

print(chessBoardCellColor(cell1, cell2))

