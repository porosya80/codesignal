def alternatingSums(a):
    first_row = sum([x for i, x in enumerate(a) if i % 2 == 0])
    second_row = sum([x for i, x in enumerate(a) if i % 2 != 0])
    return [first_row, second_row]


a = [50, 60, 60, 45, 70]
print(alternatingSums(a))
# = [180, 105]
