def lineEncoding(s):
    counter = 1
    result = ""
    for i, chr in enumerate(s[1:], 1):
        if chr == s[i-1]:
            counter += 1
        else:
            result += "" if counter == 1 else str(counter)
            result += s[i-1]
            counter = 1

    result += "" if counter == 1 else str(counter)
    result += s[-1]
    counter = 1

    return result


s = "aabbbc"
print(lineEncoding(s))
# = "2a3bc")
