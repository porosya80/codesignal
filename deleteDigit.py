def deleteDigit(n):
    res = []
    n = str(n)
    for i in range(len(n)):
        res.append(n[0:i]+n[i+1:])
    return max(res)


n = 1001
print(deleteDigit(n))
#  = 52;)
