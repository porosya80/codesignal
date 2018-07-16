def absoluteValuesSumMinimization(a):
    res = {x1: sum([abs(x-x1) for x in a]) for x1 in a}
    return min(res, key=res.get)
    

a = [2, 4, 7]
print(absoluteValuesSumMinimization(a))
# = 4
