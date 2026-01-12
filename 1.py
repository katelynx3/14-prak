import random

list = [[random.randint(1,10) for i in range(3)] for j in range(5)]
print(f'Список {list}')
max = list[0][0]
row_index = 0
col_index = 0
for i in range(len(list)):
    for j in range(len(list[i])):
        if list[i][j] > max:
            max = list[i][j]
            row_index = i
            col_index = j
print(f'''Макс значение списка {max}
Индекс строки {row_index}
Индекс позиции в строке {col_index}''')
