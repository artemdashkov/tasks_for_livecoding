"""14. Генерация случайного пароля"""
import random
import string


# way 1
def create_password(length_symbols):
    return ''.join(random.choices(string.printable, k=length_symbols))

# print(create_password(10))

# way 2
symbols = ["1","2","3","4",'a','s',"d","f"]

def create_password_2(length_passwords):
    password = "".join(random.choices(symbols, k=length_passwords))
    return password

print(create_password_2(10))
