#
# def get_multiplied_digits(number):
#     str_number = str(number)
#     if len(str_number) == 0:
#         return 1
#     first = int(str_number[0])
#     if len(str_number) == 1:
#         return first
#     return first * get_multiplied_digits(int(str_number[1:]))
#
#
# result = get_multiplied_digits(40203)
# print(result)
def summator(n):
    str_n = str(n)
    if len(str_n) == 0:
        return 0
    f = int(str_n[0])
    if len(str_n) == 1:
        return f
    return f+summator(int(str_n[1:]))


print(summator(567))
