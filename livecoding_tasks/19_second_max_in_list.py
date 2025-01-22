"""
10. Нахождение второго максимального числа в списке
"""

list_1 = [1,2,3,4,5,6,7,7]
print(f"list_1 {list_1}")

max_value = max(list_1)
list_2 = list_1.copy()
count_max_value = list_2.count(max_value)
while list_2.count(max_value) != 0:
    list_2.remove(max_value)
second_max_value = max(list_2)
print(second_max_value)
