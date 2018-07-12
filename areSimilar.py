def areSimilar(a, b):
    # print(a == b)
    flag = True

    for i in range(len(a)):
        if a[i] != b[i] and flag:

            flag = False
            if a[i] in b[i:]:
                item = b.index(a[i], i)
                b[i], b[item] = b[item], b[i]
            else:
                return False

        if a[i] != b[i]:

            return False

    return True


a = [2, 9, 6, 8, 9, 5]
b = [2, 5, 6, 8, 9, 9]
print(areSimilar(a, b))


# a = [1, 2, 3]
# b = [2, 1, 3]
# print(areSimilar(a, b) == True)


# a = [1, 2, 2]
# b = [2, 1, 1]
# print(areSimilar(a, b) == False)
