my_dict = {"a":"string",
     "b":1,
     "c":[1, 2, 3],
     "d":{"a_2":"string_2"},
     "e":(4,5,6)}

print(my_dict)

# Добавить один элемент
my_dict['f'] = 16
print(my_dict)

# Добавить несколько элементов
my_dict.update({"g": 0, "h": "string_2", "k": [6, 7, 2]})
print(my_dict)

# удалить элемент
del(my_dict['f'])
print(my_dict)

# удалить элемент
print(f"Удалить элемент метод .pop()")
key_e = my_dict.pop("e")
print(key_e)
print(my_dict)

# удалить элемент
last_element = my_dict.popitem()
last_element_2 = my_dict.popitem()
print(f"last_element:\t{last_element}")
print(f"last_element_2:\t{last_element_2}")
print(my_dict)
print(f"all keys: {my_dict.keys()}, type: {type(my_dict.keys())}")
list_of_keys = list(my_dict.keys())
print(f"list_of_keys: \t {list_of_keys}")
print(f"all values: {my_dict.values()}, type: {type(my_dict.values())}")
print(f"all items: {my_dict.items()}, type: {type(my_dict.items())}")
print(f"-----------------")
print(my_dict)
print(my_dict.get("a"))

