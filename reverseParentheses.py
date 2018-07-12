def reverseParentheses(s):
    print(s[s.rfind("("):s.find(")", s.rfind("("))+1])
    print(s[s.rfind("(")+1:s.find(")", s.rfind("("))][::-1])

    while "(" in s:
        s = s.replace(s[s.rfind("("):s.find(")", s.rfind("("))+1],
                      s[s.rfind("(")+1:s.find(")", s.rfind("("))][::-1])

    return s


s = "abc(cba)ab(bac)c"
print(reverseParentheses(s))
#  abcabcabcabc
