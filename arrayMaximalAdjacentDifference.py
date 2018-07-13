def arrayMaximalAdjacentDifference(inputArray):
    return max([abs(inputArray[i]-inputArray[i-1]) for i in range(1, len(inputArray))])


inputArray = [-1, 4, 10, 3, -2]
print(arrayMaximalAdjacentDifference(inputArray))
# = 3.
