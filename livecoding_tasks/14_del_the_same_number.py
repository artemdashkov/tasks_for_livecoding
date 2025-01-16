list_1 = [1,2,3,4,2,3]

def del_duplicate(any_list: list):
    set_from_list = set(any_list)
    new_list = list(set_from_list)
    return new_list

print(del_duplicate(list_1))