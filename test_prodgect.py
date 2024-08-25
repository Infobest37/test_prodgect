import timeit
data_1 = [9, 7, 4, 5, 6, 7, 1, 2]
data_2 = [9, 7, 4, 5, 6, 7, 1, 2, 10, 1]
data_3 = [9, 7, 4, 5, 6, 7, 1, 2, 1, 2, 3]
def sort_1(ls):
    for i in range(len(ls)-1,0,-1):
        for j in range(i):
            if ls[j] > ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]
    return ls

def sort_2(ls):
    for i in range(len(ls)-1):
        min_index = i
        for j in range(i+1,len(ls)):
            if ls[min_index] > ls[j]:
                min_index = j
                ls[j],ls[min_index] = ls[min_index],ls[j]
    return ls

def sort_3(ls):
    for i in range(1,len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j+1] = ls[j]
            j -= 1
            ls[j + 1] = key
    return ls

print(sort_1(data_1))
print(sort_1(data_2))
print(sort_1(data_3))

print(sort_2(data_1))
print(sort_2(data_2))
print(sort_2(data_3))

print(sort_3(data_1))
print(sort_3(data_2))
print(sort_3(data_3))

time_1 = timeit.timeit(lambda: sort_1(data_1.copy()), number=1000)
time_1_2 = timeit.timeit(lambda: sort_1(data_2.copy()), number=1000)
time_1_3 = timeit.timeit(lambda: sort_1(data_3.copy()), number=1000)

# Измеряем время выполнения второй версии пузырьковой сортировки
time_2 = timeit.timeit(lambda: sort_2(data_1.copy()), number=1000)
time_2_2 = timeit.timeit(lambda: sort_2(data_2.copy()), number=1000)
time_2_3 = timeit.timeit(lambda: sort_2(data_3.copy()), number=1000)

time_3 = timeit.timeit(lambda: sort_3(data_1.copy()), number=1000)
time_3_2 = timeit.timeit(lambda: sort_3(data_2.copy()), number=1000)
time_3_3 = timeit.timeit(lambda: sort_3(data_3.copy()), number=1000)

print(f"Время выполнения первой версии-1: {time_1:.5f} секунд")
print(f"Время выполнения первой версии-2: {time_1_2:.5f} секунд")
print(f"Время выполнения первой версии-3: {time_1_3:.5f} секунд")

print(f"Время выполнения второй версии-1: {time_2:.5f} секунд")
print(f"Время выполнения второй версии-2: {time_2_2:.5f} секунд")
print(f"Время выполнения второй версии-3: {time_2_3:.5f} секунд")

print(f"Время выполнения второй версии-1: {time_3:.5f} секунд")
print(f"Время выполнения второй версии-1: {time_3_2:.5f} секунд")
print(f"Время выполнения второй версии-3: {time_3_3:.5f} секунд")
def res():
     if (time_1 or time_1_2 or time_1_3 <= time_2 or time_2_2 or time_2_3 and time_1 or time_1_2 or time_1_3 <=
             time_3 or time_3_2 or time_3_3):
         return "Первая пузырьковая сортировка отсортировала быстрее"

     if (time_2 or time_2_2 or time_2_3 <= time_1 or time_1_2 or time_1_3 and time_2 or time_2_2 or time_2_3 <=
             time_3 or time_3_2 or time_3_3):
         return "Вторая пузырьковая сортировка отсортировала быстрее"
     if (time_3 or time_3_2 or time_3_3 <= time_1 or time_1_2 or time_1_3 and time_3 or time_3_2 or time_3_3 <=
             time_2 or time_2_2 or time_2_3):
         return "Третья пузырьковая сортировка отсортировала быстрее"

print(res())

