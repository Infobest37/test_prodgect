def print_params(a = 1, b = 'строка', c = None):
    print(a, b, c)

values_list = ["a,b,c,d,r"]
values_dict = {"d": 1, "v": 5,"s": 7}
values_list_2 = [4,67]
print_params(values_list, values_dict)
def print_params1(**kyi):
    print(kyi)
values_list_2 = {"a":4,"b":67}
print_params1(**values_list_2)
