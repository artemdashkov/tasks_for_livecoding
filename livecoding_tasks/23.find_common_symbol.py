"15. Поиск общего элемента в двух списках"

# way 1
list_1 = [1,2,3,4,5,5]
list_2 = [5,6,7,8,9]

# way 1

# set_1 = set(list_1)
# set_2 = set(list_2)
#
# intersection = set_1 & set_2
# print(intersection)


# way 2
for x in list_1:
    for y in list_2:
        if x == y:
            print(x)
