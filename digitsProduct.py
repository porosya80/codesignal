def digitsProduct(product):
    count = 9
    res = 1
    while res < 10000:
        count += 1
        res = 1
        for i in str(count):
            res = res * int(i)
        if res == product:
            break
    else:
        return -1

    return count



product = 450
print(digitsProduct(product))
#  = 26
