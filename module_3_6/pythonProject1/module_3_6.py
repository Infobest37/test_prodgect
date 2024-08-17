# import tkinter as tk
#
# def get_values():
#     num2= int(number2_entry.get())
#     num3= int(number3_entry.get())
#     return num2,num3
#
# def insert_values(value):
#     answer_entry.delete(0, tk.END)
#     answer_entry.insert(0, value)
# def add():
#     num2,num3= get_values()
#     result = num2 + num3
#     insert_values(result)
#
# def subtract():
#     num2,num3= get_values()
#     result = num2 - num3
#     insert_values(result)
#
# def multiply():
#     num2,num3= get_values()
#     result = num2 * num3
#     insert_values(result)
#
# def divide():
#     num2,num3= get_values()
#     result = num2 / num3
#     insert_values(result)
#
#
#
#
# window = tk.Tk()
# window.title('Калькулятор')
# window.geometry('500x300')
# window.resizable(False, False)
# button_add = tk.Button(window, text = "+", width=2, height=1, command=add)
# button_add.place(x= 100, y = 100 )
# button_min = tk.Button(window, text = "-", width=2, height=1, command=subtract)
# button_min.place(x= 100, y = 150 )
# button_mul = tk.Button(window, text = "*", width=2, borderwidth=1, height=1, command=multiply)
# button_mul.place(x= 100, y = 200 )
# button_div = tk.Button(window, text = "/", width=2, borderwidth=1, height=1, command=divide)
# button_div.place(x= 100, y = 250 )
#
# answer_entry = tk.Entry(window, width=30, borderwidth=5 )
# answer_entry.place(x= 200, y = 50 )
# number2_entry = tk.Entry(window, width=30)
# number2_entry.place(x= 200, y = 150 )
#
# number3_entry = tk.Entry(window, width=30)
# number3_entry.place(x= 200, y = 200 )
#
# number2 = tk.Label(window, text = "Введите первое число" )
# number2.place(x= 200, y = 125 )
# number3 = tk.Label(window, text = "Введите второе число" )
# number3.place(x= 200, y = 175 )
# number1 = tk.Label(window, text = "Ответ" )
# number1.place(x= 200, y = 25 )
#
# window.mainloop()
#
#
#
#


def calculate_structure_sum(data_structure):
    sum_1 = 0

    # Если элемент - число, просто добавляем его к сумме
    if isinstance(data_structure, (int, float)):
        sum_1 += data_structure

    # Если элемент - строка, добавляем её длину к сумме
    elif isinstance(data_structure, str):
        sum_1 += len(data_structure)

    # Если элемент - список, кортеж или множество, рекурсивно обрабатываем каждый элемент
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            sum_1 += calculate_structure_sum(item)

    # Если элемент - словарь, обрабатываем его ключ и значение и плюсуем
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum_1 += calculate_structure_sum(value)
            sum_1 += calculate_structure_sum(key)

    return sum_1


# Пример использования

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)

