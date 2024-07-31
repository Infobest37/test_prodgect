first = int(input("Введите любое число : "))
second = int(input("Введите любое число : "))
third = int(input("Введите любое число : "))


if first == second and second == third and third == first:
    print(f"Все три числа совпали")
elif first != second and second == third or third == first:
    print(f"Совпали только 2 числа ")
elif first == second and second != third or third == first:
    print(f"Совпали только 2 числа ")
elif first == second or second == third and third != first:
    print(f"Совпали только 2 числа ")
else:
    print(f"Ни одно число не совпало поэтому ваше число: ")