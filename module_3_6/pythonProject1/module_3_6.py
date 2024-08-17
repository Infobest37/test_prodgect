
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

