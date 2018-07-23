def fileNaming(names):
    outnames = []
    for name in names:
        if name in outnames:
            k = 1
            while "{}({})".format(name, k) in outnames:
                k += 1
            name = "{}({})".format(name, k)
        outnames.append(name)
    return outnames


names = ["doc", "doc", "image", "doc(1)", "doc"]
print(fileNaming(names))
# ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"
