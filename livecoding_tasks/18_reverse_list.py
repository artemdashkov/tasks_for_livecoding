"""
9. Разворот списка
"""
from livecoding_tasks.check_polindrom import reverse_string

list_1 = list(range(0,11))
print(list_1)
print(list_1[::-1])

"""
9. Разворот строки
"""

string = "string"

list_of_string = []
for x in string:
    list_of_string.append(x)
list_of_string.reverse()

reverse_string = ""
for x in list_of_string:
    reverse_string += x

print(reverse_string)