"""
Необходимо развернуть строку
"""

stroka = "stroka"

# first solution
def reverse_string(string):
    reverse_string = ""
    for x in range(len(string)-1, -1, -1):
        reverse_string += string[x]
    return reverse_string

# second solution
def reverse_string_2(string):
    list_letters = []
    for letter in string:
        list_letters.append(letter)
    list_letters.reverse()
    reverse_string = ""
    for letter in list_letters:
        reverse_string += letter

    return reverse_string
