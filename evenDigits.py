
def evenDigitsOnly(n):
    return all([not int(x) % 2 for x in str(n)])

def evenDigitsOnly_(n):
    return not sum([x for x in n]) % 2


print(evenDigitsOnly_(247622))
