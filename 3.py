import random

row = 3
col = 5
min_ = -10
max_ = 10
random_str = [[random.randint(min_, max_) for _ in range(col)] for _ in range(row)]
print(f'Изначальный список {random_str}')

list_ = []
for i in range(row):
    for j in random_str[i]:
        if j > 0:
            list_.append(j)
print(f'Список с положительными элементами {list_}')
