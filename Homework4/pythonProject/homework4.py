#homework6.py
my_dict = {"sist_1": "diagnostics", "sist_2": "calculation", "sist_3": "project"}
print(my_dict)
print(my_dict["sist_1"], my_dict.get("sist_4","Такого ключа нет"))
my_dict.update({"sist_5": 12345, "sist_6": 6769})
print(my_dict)
my_dict.pop("sist_1")
print(my_dict)

my_set = {1, 2, 3, 4, 1, 2, 2, 4, 3, 2, 4}
print(my_set)
my_set.update({7,8})
print(my_set)
my_set.discard(7)
print(my_set)