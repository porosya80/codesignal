def palindromeRearranging(inputString):
    result = [True if not (inputString.count(x) % 2) else False for x in set(inputString)]

    return True if result.count(False) < 2 else False


def palindromeRearranging_smart(inputString):

    return sum([inputString.count(i) % 2 for i in set(inputString)]) <= 1



inputString = "abbcabb"
print(palindromeRearranging(inputString))
