list_1 = list(range(1001)) # [0, 1, 2, ... 1000]

def find_number(x):
    find_number = None
    index_lower = list_1[0] # 0
    index_higher = list_1[-1] # 1000
    index_half_of_list = len(list_1) // 2 # 500

    find_number = list_1[index_half_of_list] # list_1[500] > 500
    count = 0
    # while x != find_number:
    while count != 10:
        count += 1
        if x > find_number: # x = 700
            index_lower = index_half_of_list # стало 500, было index_lower = 0
            len_list = len(list_1[index_lower:index_higher]) // 2 # [500:1000] > 500 // 2 > 250
            index_half_of_list = index_half_of_list + len_list # 500 + 250 > 750
            find_number = list_1[index_half_of_list] # list_1[750] > 750
            print(f"index_lower {index_lower}")
            print(f"index_half_of_list {index_half_of_list}")
            print(f"index_higher {index_higher}\n")
        elif x < find_number: # x = 700
            index_higher = index_half_of_list # 750
            len_list = len(list_1[index_lower:index_half_of_list]) // 2 # 500:750 > 250 // 2 > 125
            index_half_of_list = index_half_of_list - len_list # 750 - 125 > 625
            find_number = list_1[index_half_of_list]
            print(f"index_lower {index_lower}")
            print(f"index_half_of_list {index_half_of_list}")
            print(f"index_higher {index_higher}\n")
    print(f"find_number is {find_number}")

find_number(833)