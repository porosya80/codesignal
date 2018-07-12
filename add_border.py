def addBorder(picture):
    pic_with_border = ["*"+row.center() + "*" for row in picture]
    pic_with_border.insert(0, "*"*len(pic_with_border[0]))
    pic_with_border.append("*"*len(pic_with_border[0]))
    return pic_with_border


picture = ["abc",
           "ded"]

addBorder(picture)

# = ["*****",
#   "*abc*",
#   "*ded*",
#   "*****"]
