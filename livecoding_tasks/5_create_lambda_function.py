"""
лямбда функция, которая возвращает сумму двух чисел
"""
add_two_numbers = lambda x, y: x+y
result_add_two_numbers = add_two_numbers(5, 6)
print(result_add_two_numbers)

"""
лямбда функция, которая возвращает True или False, в зависимости от того, 
является ли переданное число четным или нет
"""
lambda_ostatok = lambda x: x % 2 == 0
result_1 = lambda_ostatok(4)
print(result_1)

mult_2 = lambda x: x*2
print(mult_2(4))



area_rectangle = lambda x, y: x*y
a_1 = area_rectangle(10, 2)
print(f"area_rectangle a_1: {a_1}")