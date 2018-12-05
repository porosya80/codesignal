def containsCloseNums(nums, k):
    result = False
    index_table = {}
    for index, i in enumerate(nums):
        if i not in index_table.keys():
            index_table[i] = index
        else:

            # print(f"hello {index} ")
            # print(f'index - {index}, dict = {index_table[i]}')
            if index - index_table[i] <= k:
                result = True
            index_table[i] = index

    return result


nums = [1, 0, 1, 1]
k = 1

print(containsCloseNums(nums, k))
