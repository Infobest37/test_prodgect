numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
minus = []
plus = []
for i in list(numbers):
    if i % 2 != 0:
        minus.append(i)

    else:
        plus.append(i)

print(minus)
print(plus)
