def allLongestStrings(inputArray):

    print(len(max(inputArray, key=len)))
    return [str for str in inputArray if len(str) == len(max(inputArray, key=len))]


inputArray = ["aba", "aa", "ad", "vcd", "aba"]

print(allLongestStrings(inputArray))
# = ["aba", "vcd", "aba"]
