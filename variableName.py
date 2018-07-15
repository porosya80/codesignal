def variableName(name):
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)] + ["_"] + [str(x) for x in range(10)]
    if name[0].isdigit():
        return False
    return all([True if x in alphabet else False for x in name.lower()])

    # return True
name = "var_1_-_Int"

name.isidentifier
print(variableName(name))
