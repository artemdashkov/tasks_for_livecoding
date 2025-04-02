# 27. Поиск первого неповторяющегося символа

list_1 = [1, 1, 1, 1]

for x in range(len(list_1)):
    if x == max(range(len(list_1))):
        print(f"В последовательности нет неповторяющихся символов")
        break
    elif list_1[x] == list_1[x+1]:
        continue
    else:
        print(f"Первый неповторяющейся символ: {list_1[x+1]}")
        break