# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

a = int(input("Введите количество арбузов:"))
import random
array = random.sample(range( 1, 10), a)
print(array)
for i in  array:
    big = max(array)
    small = min(array)
print(f'Самый тяжелый арбуз весит {big} килограмм, а самый легкий {small}')

