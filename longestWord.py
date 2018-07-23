def longestWord(text):
    for item in "![]\{}\"\'.,?_-":
        text = text.replace(item, " ")
    return(max(text.split(), key=len))


text = "A!! AA_z"
print(longestWord(text))
# ="steady")
