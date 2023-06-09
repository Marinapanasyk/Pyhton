# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
import random
k = int(input("Введите количество кустов на грядке:"))
a = list(random.randint(0, 10) for i in range(k))
result = []
i = 0
sum = 0
print(a)

while (i < k):
    if (i == k - 1):
        sum = a[i] + a[i - 1] + a[0]
    else:
        sum = a[i] + a[i - 1] + a[i + 1]
        result.append(sum)
        result.sort()
    i += 1
print(result)
result.sort()
print(f"максимальное число ягод за одну итерацию {result[-1]}")



