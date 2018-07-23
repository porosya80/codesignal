import re
def isMAC48Address(inputString):
    return True if re.fullmatch(r"^([0-9A-F]{2}[:-]){5}([0-9A-F]{2})$", inputString) else False
