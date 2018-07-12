def arrayChange(inputArray):
    counter = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] > inputArray[i-1]:
            pass
        else:
            tmp = (inputArray[i-1]+1)-inputArray[i]
            counter += tmp
            inputArray[i] += tmp
    return counter


inputArray =  [-1000, 0, -2, 0]
print(arrayChange(inputArray))
