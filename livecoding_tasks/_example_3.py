list_1 = list(range(1001)) # [0, 1, 2, ... 1000]
index_lower = list_1[0] # 0
index_higher = list_1[-1] # 1000

len_list = len(list_1[index_lower:index_higher]) // 2
print(len_list)
