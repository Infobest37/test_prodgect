first = int(input("Введите любое число : "))
second = int(input("Введите любое число : "))
third = int(input("Введите любое число : "))


if first == second == first:
    print(f"Совпали только 2 числа ")
elif first == second or second == third or third == first:
    print(f"Все три числа совпали")

else:
    print(f"Ни одно число не совпало поэтому ваше число: ", 0)