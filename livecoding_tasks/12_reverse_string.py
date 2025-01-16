def reverse_string(string: str) -> str:
    string_list = list(string)
    # string_list.reverse()
    string_list = string_list[::-1]
    reverse_string = ""
    for x in string_list:
        reverse_string += x
    return reverse_string

print(reverse_string("sobaka"))