def messageFromBinaryCode(code):
    res = ''
    for i in range(0, len(code), 8):
        # print(code[i:i+8])
        # print((bytearray(code[i:i+8], 'ascii').decode('utf-8')))
        res += (chr(int(code[i:i+8], 2)))
    return res


code = "010010000110010101101100011011000110111100100001"


# """
#             01001000
#             01100101
#             01101100
#             01101100
#             01101111
#             00100001
#             """
print(messageFromBinaryCode(code))
#  = "Hello!"
