""""
6. Нахождение минимального и максимального элементов в списке
"""

list_1 = [1,2,3,4,5]

def find_max_and_min(any_list):
    max_value = max(list_1)
    min_value = min(list_1)
    return f"max_value: {max_value}, min_value: {min_value}"

print(find_max_and_min(list_1))