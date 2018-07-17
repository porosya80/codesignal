# def isBeautifulString(a):
#     flag = True
#     alpha = list(map(chr, range(97, 123)))
#     for i in range(1, len(alpha)):
#         if alpha[i] in a:
#             if alpha[i-1] in a and a.count(alpha[i]) <= a.count(alpha[i-1]):
#                 pass
#             else:
#                 flag = False

#     return flag

import string


def isBeautifulString(inputString):

    r = [inputString.count(i) for i in string.ascii_lowercase]
    print(r)
    print(sorted(r, reverse=True))
    return r == sorted(r, reverse=True)


inputString = "abbcc"
print(isBeautifulString(inputString))
