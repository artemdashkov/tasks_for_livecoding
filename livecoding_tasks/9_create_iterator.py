list_1 = [1,2,3]
dict_1 = {"one":1,
          "two":2,
          "three":3,}
iterator_list = iter(list_1)
iterator_dict = iter(dict_1)
print(iterator_list)
print(iterator_dict)
for x in iterator_list:
    print(x)

for y in iterator_dict:
    print(y)
for z in list_1.__iter__():
    print(z)

list_2 = [4,5,6]
list_2_iterator = iter(list_2)
print(f"\n{list_2_iterator.__next__()}")
print(f"{list_2_iterator.__next__()}")
print(f"{list_2_iterator.__next__()}")