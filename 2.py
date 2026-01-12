import random

row = 3
col = 5
min_ = 1
max_ = 10
random_str = [[random.randint(min_, max_) for _ in range(col)] for _ in range(row)]
print(f'Список {random_str}')
biggest_ = 0
list_ = []
for i in range(row):
    list_sum = 0
    for j in random_str[i]:
        list_sum += j
    list_.append(list_sum)
    if list_sum > biggest_:
        biggest_ = list_sum
print(f'Сумма элементов каждой подстроки {list_}')
