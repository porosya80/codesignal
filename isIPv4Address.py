def isIPv4Address(inputString):
    result = [True if 255 >= int(x) >= 0 else False for x in inputString.strip().split('.') if x.isdecimal()]
    return True if len(result) == 4 and all(result) else False


inputString = "254..170.255"
print(isIPv4Address(inputString))
