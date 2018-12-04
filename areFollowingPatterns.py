def areFollowingPatterns(strings, patterns):
    result = True
    string_to_pattern = {}
    pattern_to_string = {}
    for string, pattern in zip(strings, patterns):
        # print(string, pattern)
        if string not in string_to_pattern.keys():
            string_to_pattern[string] = pattern
        if pattern not in pattern_to_string.keys():
            pattern_to_string[pattern] = string

    for string, pattern in zip(strings, patterns):
        # print(string_to_pattern[string], pattern_to_string[pattern])
        if string_to_pattern[string] != pattern or pattern_to_string[pattern] != string:
            result = False
            break

    return result


strings = ["cat",
           "dod",
           "dod"]
patterns = ["a",
            "b",
            "b"]
areFollowingPatterns(strings, patterns)
# Expected Output:
# true
