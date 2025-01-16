def reverse_string(test_data: str):
    test_data_list = list(test_data)
    test_data_list.reverse()
    reverse_string = ""
    for x in test_data_list:
        reverse_string += x
    return reverse_string

def check_polindrom(test_data: list):
    type_test_data = type(test_data) # str, int, list
    if type_test_data == str:
        result = reverse_string(test_data)
        return result
    elif type_test_data == list:
        return test_data[::-1]
    elif type_test_data == int:
        test_data_string = str(test_data)
        test_data_string_reverse = reverse_string(test_data_string)
        return int(test_data_string_reverse)
    elif type_test_data == tuple:
        test_data_list = list(test_data)
        test_data_list_reverse = test_data_list[::-1]
        return tuple(test_data_list_reverse)

print(check_polindrom("string"))
print(check_polindrom([1, 2, 3]))
print(check_polindrom(45))
print(check_polindrom((458, 345)))

def just_list(data):
    assert data == data[::-1]