def sortByHeight(a):
    trees = []
    for i, item in enumerate(a):
        if item == -1:
            trees.append(i)
    for _ in trees:
        a.remove(-1)
    a = sorted(a)
    for tree in trees:
        a.insert(tree, -1)
    return a


a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(a))
# [-1, 150, 160, 170, -1, -1, 180, 190]
