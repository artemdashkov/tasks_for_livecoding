# Проверка, является ли строка числом

string_1 = "la"
string_2 = 5
string_3 = 5.1
string_4 = ["1", "list"]
string_5 = ('a', 5)
string_6 = {"string_6": 5}


def check_number_or_string(text_or_number):
    if type(text_or_number) is str:
        print(f"{text_or_number}\t: is string")
    elif type(text_or_number) is int:
        print(f"{text_or_number}\t: is int")
    elif type(text_or_number) is float:
        print(f"{text_or_number}\t: is float")
    else:
        print(f"{text_or_number}\t: is not string, int or float")

check_number_or_string(string_1)
check_number_or_string(string_2)
check_number_or_string(string_3)
check_number_or_string(string_4)
check_number_or_string(string_5)
check_number_or_string(string_6)