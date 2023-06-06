# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
a = list(random.randint(-100, 100) for i in range(10))
print(a)
min_number = int(input("Введите минимальное значение диапазона:"))
max_number = int(input("Введите максимальное  значение диапазона:"))
for i in range(len(a)):
    if min_number <= a[i] <= max_number:
        print(i)
