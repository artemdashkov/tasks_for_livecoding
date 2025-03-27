# 16. Удаление всех пробелов из строки
string_1 = "delete all space from string"

new_string = ""
for x in string_1:
    if x == " ":
        continue
    new_string += x

print(new_string)