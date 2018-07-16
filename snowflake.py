n = 7
a = [["." for n in range(n)] for y in range(n)]

for i in range(n):
    a[i][(len(a[0]))//2] = "*"

    for j in range(n):
        a[(len(a[0]))//2][j] = "*"
        a[i][i] = "*"
        if i+j+1 == n:
            a[i][j] = "*"


for row in a:
    print(' '.join([str(elem) for elem in row]))
