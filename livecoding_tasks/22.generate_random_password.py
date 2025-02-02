"""14. Генерация случайного пароля"""
import random
import string

def create_password(length_symbols):
    return ''.join(random.choices(string.printable, k=length_symbols))

print(create_password(10))
