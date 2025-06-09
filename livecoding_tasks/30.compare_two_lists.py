# 30. Сравнение двух списков

list_1 = [4, 2, 3, 1]
list_2 = [7, 3, 4, 5, 6]


print(list_1 == list_2)
list_1.sort()
print(list_1)
print(sorted(list_2))
print(list_2)
print(list_1.sort() == list_2.sort())