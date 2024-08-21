import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    num3 = int(number3_entry.get())
    num4 = int(number4_entry.get())
    result1 = num1 * 60 + num2
    result2 = num3 * 60 + num4
    return num1, num2, num3, num4, result1, result2
def insert_values(value1, value2):
    answer_entry_h.delete(0, tk.END)
    answer_entry_h.insert(0, value1 )
    answer_entry_m.delete(0, tk.END)
    answer_entry_m.insert(0, value2)


def add_time():
    num1, num2, num3, num4, result1, result2 = get_values()
    result3 = (result1 + result2)//60
    result4 = (result1 + result2) % 60
    insert_values(result3,result4)

def sub():
    num1, num2, num3, num4, result1, result2 = get_values()
    result3 = (result1 - result2)//60
    result4 = (result1 - result2) % 60
    insert_values(result3,result4)

def mul():
    num1, num2, num3, num4, result1, result2 = get_values()
    result3 = (result1 * result2)//60
    result4 = (result1 * result2) % 60
    insert_values(result3,result4)

def div():
    num1, num2, num3, num4, result1, result2 = get_values()
    result3 = (result1 / result2)//60
    result4 = (result1 / result2) % 60
    insert_values(result3,result4)


window = tk.Tk()
window.title("Калькулятор времени")
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=2, height=2, command=add_time)
button_add.place(x=100, y=120)
button_sub = tk.Button(window, text="-", width=3, height=2, command=sub)
button_sub.place(x=150, y=120)
button_mul = tk.Button(window, text="*", width=4, height=2, command=mul)
button_mul.place(x=200, y=120)
button_div = tk.Button(window, text="/", width=5, height=2, command=div)
button_div.place(x=250, y=120)
number1_entry = tk.Entry(window, width=15)
number1_entry.place(x=75, y=75)
number1 = tk.Label(window, text = "Часы")
number1.place(x=95, y=50)
number2_entry = tk.Entry(window, width=15)
number2_entry.place(x=200, y=75)
number2 = tk.Label(window, text = "Минуты")
number2.place(x=200, y=50)

number3_entry = tk.Entry(window, width=15)
number3_entry.place(x=75, y=200)
number3 = tk.Label(window, text = "Часы")
number3.place(x=95, y=175)
number4_entry = tk.Entry(window, width=15)
number4_entry.place(x=200, y=200)
number4 = tk.Label(window, text = "Минуты")
number4.place(x=200, y=175)


answer_entry_h = tk.Entry(window, width=10, borderwidth=5)
answer_entry_h.place(x=80, y=295)

answer_entry_m = tk.Entry(window, width=10, borderwidth=5)
answer_entry_m.place(x=215, y=295)


answer= tk.Label(window, text="Ответ")
answer.place(x=170, y=250)
answer= tk.Label(window, text="Часы")
answer.place(x=100, y=270)
answer= tk.Label(window, text="Минуты")
answer.place(x=220, y=270)


window.mainloop()