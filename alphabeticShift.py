def alphabeticShift(inputString):
    return [chr(ord(x)+1) if x!="z" else 'a' for x in inputString]