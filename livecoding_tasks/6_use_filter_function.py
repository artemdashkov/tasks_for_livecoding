"""
Получить из списка чисел только четные числа
"""
from datetime import datetime
start_time = datetime.now()
list_numbers = set(range(80000000))

# Первое решение с использованием функции с циклом for
list_of_even = []
def is_even(list_num):
    for num in list_num:
        if num % 2 == 0:
            list_of_even.append(num)
        else:
            pass
    return list_of_even


even_numbers_list = is_even(list_numbers)

# Второе решение с использованием функции и метода filter()
# def is_even_2(num):
#     return num % 2 == 0

# even_numbers = filter(is_even_2, list_numbers)
# even_numbers_list = list(even_numbers)

# even_numbers = list(filter(lambda x: x % 2 == 0, list_numbers))


end_time = datetime.now()
result_time = end_time - start_time
print(result_time)