def chessBoardCellColor(cell1, cell2):
    board = 'abcdefgh'.upper()
    return (board.index(cell1[0])+1+int(cell1[1])) % 2 == (board.index(cell2[0])+1+int(cell2[1])) % 2


cell1 = "A1"
cell2 = "C3"

print(chessBoardCellColor(cell1, cell2))

# list1 = [int(input()) for i in range(6)]

# list1 = [1, 5, 7, 5, 1, 10]
# list1 = [1, 5, 7, 10, 1,10]
# lll = [print(x) for x in set(list1) if list1.count(x) < 2]
# range()

# Read an integer:
# a = int(input())
# for n in range(1, a+1):
# [print(x, end="") for x in range(1, 4+1) for n in range(1, 4)]
# # print()
# a = "1 2 3 4 5".split()

# for i in range(1, len(a), 2):
#     print(a[i])
#     print(a[i-1])
#     a[i], a[i-1] = a[i-1], a[i]

# print(a)
count = 5
print((count * (count - 1))/2)
