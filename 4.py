import random

row = 3
col = 5
min_ = 1
max_ = 10
random_str = [[random.randint(min_, max_) for _ in range(col)] for _ in range(row)]
print(f'Список {random_str}')
search = int(input('Введите число для поиска '))

found = False
for i in range(len(random_str)):
    for j in range(len(random_str[i])):
        if random_str[i][j] == search:
            print(f'Введеное число найдено в строке {i} в позиции {j}')
            found = True
if not found:
    print('Не найден')
