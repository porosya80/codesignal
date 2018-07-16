from itertools import permutations

def stringsRearrangement(inputArray):
    poss = permutations(inputArray)
    for array in poss:
        if chk_arr(array):
            return True
    return False
        
def chk_arr(arr):
    for i in range(len(arr) - 1):
        if sum([a != b for a, b in zip(arr[i], arr[i + 1])]) != 1:
            return False
    return True







inputArray = ["aba", "bbb", "bab"]
print(stringsRearrangement(inputArray))
# = false
