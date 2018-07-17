def buildPalindrome(st):
    res = st
    counter = 0
    while res != res[::-1]:
        res = st+st[counter::-1]
        counter +=1 
    return res







st = "abaa"
print(buildPalindrome(st)) 
# = "abcdcba"
