"""
    Найти максимум в массиве со строками.
    Если элемент можно перевести в число - его стоит учитывать.
"""

def max_in_mixed_array(array: list[int | str]) -> int | None:
    list_int = []
    for x in array:
        try:
            x = int(x)
            list_int.append(x)
        except:
            continue
    if len(list_int) != 0:
        return max(list_int)
    return None


assert max_in_mixed_array([1, 2, 3]) == 3
assert max_in_mixed_array(["5", "7"]) == 7
assert max_in_mixed_array([3, "abc", "-2", "0x57"]) == 3
assert max_in_mixed_array(["abc", "-2", "0x57"]) == -2
assert max_in_mixed_array(["abc", "--2", "0x57"]) == None