def extractEachKth(inputArray, k):
    return([x for i, x in enumerate(inputArray) if (i+1) % k])


inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(extractEachKth(inputArray, k))
# = [1, 2, 4, 5, 7, 8, 10])
