def arrayMaxConsecutiveSum(a, k):
    res = [sum(a[0:k])]
    for i in range(1, len(a)-k+1):
        res.append(res[i-1]-a[i-1]+a[i+k-1])
    
    return(max(res))
    

inputArray = [1, 3, 2, 4]
k = 3
# , the output should be
print(arrayMaxConsecutiveSum(inputArray, k))
# = 9.
# All possible sums of 2 consecutive elements are:

# 2 + 3 = 5
# 3 + 5 = 8
# 5 + 1 = 6
# 1 + 6 = 7.
# Thus, the answer is 8.
