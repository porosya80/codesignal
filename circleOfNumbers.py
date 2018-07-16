def circleOfNumbers(n, firstNumber):
     return firstNumber+n//2 if firstNumber+n//2 <= n-1 else abs(-firstNumber+n//2)



n = 10  
firstNumber = 2
print(circleOfNumbers(n, firstNumber))
#  = 7.
