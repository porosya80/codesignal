

board = [["." for i in range(1, 9)] for j in range(1, 9)]


def draw_board(quin, moves):
    # print("0 1 2 3 4 5 6 7 8")
    global board

    for move in moves:
        # print(move)
        x, y = move
        board[y-1][x-1] = "x"

    # for quin in quins:
    x, y = quin
    if board[y-1][x-1] != "x":
        board[y-1][x-1] = "Q"
    else:
        print("quin is not safe")


#    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in A]))
    # for i in range(1,9) :
    #     print()
    #     for j in range(1,9):
    #         print(".",end=" ")
    # print()
    print("\n".join([" ".join([item for item in row]) for row in board[::-1]]))


# quins = [(int(x), int(y)) for x, y in input().split() for i in range(8)]

# print(quins)
# quins = [(x, y) for x, y in [(1, 5), (2, 3), (3, 1), (4, 7), (5, 2), (6, 8), (7, 6), (8, 4)]]
quins = [(1, 5), (2, 3), (3, 1), (4, 7), (5, 2), (6, 8), (7, 6), (8, 4)]
# quins = [(4, 4),]
# print(quins)
# generate possible moves
all_moves = []
for quin in quins:
    if quin in all_moves:
        print("YES")
        break
    qx, qy = quin
    moves = []
    # make row
    moves = ([(qx, y) for y in range(1, 9)])
    # make column
    moves.extend([(x, qy) for x in range(1, 9)])
    # diagonal
    moves.extend([(x, y) for x, y in zip(range(qx, 9, 1), range(qy, 9, 1))])
    moves.extend([(x, y) for x, y in zip(range(qx, 9, 1), range(qy, 0, -1))])
    moves.extend([(x, y) for x, y in zip(range(qx, 0, -1), range(qy, 9, 1))])
    moves.extend([(x, y) for x, y in zip(range(qx, 0, -1), range(qy, 0, -1))])
    while quin in moves:
        moves.remove(quin)
    all_moves.extend(moves)

else:
    print("NO")

    # print(quin)
    # draw_board(quin, moves)
    # all_moves.extend(moves)
    # # for move in moves:
    # if move in all_moves:
    #     Flag = False
    #     print("YES")
    #     break
    # else:
    #     all_moves.append(move)


# print(all_moves)
# print((8, 8) in all_moves)
