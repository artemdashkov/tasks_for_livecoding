
list_1 = [1, 2, 3, 4]
print(sum(list_1))

def sum_number(any_list):
    result = 0
    for x in any_list:
        result += x
    return result

print(sum_number(list_1))