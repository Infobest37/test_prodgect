def print_params(a = 1, b = 'строка', c = None):
    print(a, b, c)


print_params(b = 25)
print_params(c = [1,2,3])
values_list = ["a,b,c", 1234, True]
values_dict = {'a': 1, 'b': 5,'c': 7}
values_list_2 = ["srt", 23]
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)

def print_params1(**kyi):
    print(kyi)
values_list_2 = {"a":4,"b":67}
print_params1(**values_list_2)
values_list_2 = [4,67]