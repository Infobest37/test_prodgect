def divide(first, second):
    try:
        result = first/second
    except ZeroDivisionError:
        return "Ошибка"
    return result
# print(divide(2, 2))




