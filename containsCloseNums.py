def containsCloseNums(nums, k):
    result = False
    index_table = {}
    for index, i in enumerate(nums):
        if i not in index_table.keys():
            index_table[i] = index
        else:
            if index - index_table[i] <= k:
                result = True
                break

    return result


nums = [0, 1, 2, 3, 5, 2]
k = 3

print(containsCloseNums(nums, k))
