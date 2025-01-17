list_1 = list(range(1000))

def find_number(x):
    find_number = None
    index_lower = list_1[0]
    index_higher = list_1[:-1]
    index_half_of_list = len(list_1) // 2

    find_number = list_1[index_half_of_list]
    count = 0
    # while x != find_number:
    while count != 10:
        count += 1
        if x > find_number:
            print(f"current find_number is {find_number}")
            index_lower = index_half_of_list
            len_list = len(list_1[index_half_of_list:index_higher]) // 2
            index_half_of_list = index_half_of_list + len_list
            find_number = list_1[index_half_of_list]
        elif x < find_number:
            print(f"current find_number is {find_number}")
            index_higher = index_half_of_list
            len_list = len(list_1[index_lower:index_half_of_list]) // 2

            index_half_of_list = index_half_of_list - len_list
            find_number = list_1[index_half_of_list]
    print(f"find_number is {find_number}")

find_number(700)