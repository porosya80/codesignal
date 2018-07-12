def areSimilar(a, b):
    list1 = []
    list2 = []
    for i in range(len(a)):
        if a[i] != b[i]:
            list1.append(a[i])
            list2.append(b[i])
    if len(list1) < 2 and set(list1) == set(list2):
        return True
    else:
        return False


def areSimilar_smart(a, b):
    return sorted(a) == sorted(b) and sum(i != j for i, j in zip(a, b)) < 3


a = [1, 2, 2]
b = [2, 1, 1]
print(areSimilar(a, b))


# a = [1, 2, 3]
# b = [2, 1, 3]
# print(areSimilar(a, b) == True)


# a = [1, 2, 2]
# b = [2, 1, 1]
# print(areSimilar(a, b) == False)
