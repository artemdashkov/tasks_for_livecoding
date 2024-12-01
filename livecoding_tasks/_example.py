from datetime import datetime
import random

def decorator_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        print(f"start_time: \t{start_time}")
        func(*args, **kwargs)
        end_time = datetime.now()
        print(f"start_time: \t{end_time}")
        total_time = end_time - start_time
        print(f"total_time: \t{total_time}")
    return wrapper

@decorator_time
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

@decorator_time
def max_in_mixed_array_2(array: list[int | str]) -> int | None:
    answer = None
    for i in array:
        try:
            as_int = int(i)
            if answer is None or as_int > answer:
                answer = as_int
        except ValueError:
            pass
    return answer

@decorator_time
def max_in_mixed_array_3(array: list[int | str]) -> int | None:
    """
        Найти максимум в массиве со строками.
        Если элемент можно перевести в число - его стоит учитывать.
    """

    # Решение:
    # print(array)
    new_arr = []
    for i in array:
        if isinstance(i, int):
            new_arr.append(i)
        else:
            try:
                new_arr.append(int(i))
            except ValueError:
                pass

    if len(new_arr) == 0:
        # print('None')
        return None
    else:
        # print(new_arr)
        # print(max(new_arr))
        return max(new_arr)

@decorator_time
def max_in_mixed_array_4(array: list[int | str]) -> int | None:
    """
        Найти максимум в массиве со строками.
        Если элемент можно перевести в число - его стоит учитывать.
    """

    # Решение:
    # print(array)
    answer = None
    count = 0
    for i in array:
        while answer is None:
            count += 1
            if isinstance(i, int):
                    answer = i
            elif isinstance(i, str):
                try:
                    i = int(i)
                    answer = i
                except ValueError:
                    pass
            else:
                pass
        break

    for i in array[count:]:
        if isinstance(i, int):
                answer = i
        elif isinstance(i, str):
            try:
                i = int(i)
                answer = i
            except ValueError:
                pass
        else:
            pass

    return answer

# list_1 = list(range(50000000))
list_1 = [random.randint(1, 10000) for _ in range(10000000)]

# max_in_mixed_array(list_1)
# max_in_mixed_array_2(list_1)
# max_in_mixed_array_3(list_1)
max_in_mixed_array_4(list_1)