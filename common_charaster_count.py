def commonCharacterCount(s1, s2):
    str1 = list(s1)
    str2 = list(s2)
    count = 0
    while str1:
        to_find = str1.pop(0)
        if to_find in str2:
            count += 1
            str2.remove(to_find)
    return(count)

s1 = "aabcc"
s2 = "adcaa"
commonCharacterCount(s1, s2)
