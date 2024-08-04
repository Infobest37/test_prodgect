def pairs(first, n):
    g_result = ""
    for second in range(first + 1, n):
        if n % (first + second) == 0:
            g_result += F"{first}{second}"
    return g_result

def result(a):
    g_result = "" # пустая страка куда будем добавлять символы
    for i in range(1, a): # ренж это диапозон числа в функции
        g_result += pairs(i, a)
    return g_result
for number in range(3, 21):
    print(number, result(number))