#Цикл or:

lst = [1, 3, 4, 2, 0, 123, 321, 222]

for aaa in lst:
    print(aaa)

for letter in 'Это строка. Она тоже последовательность':
    print(letter, end='; ')

# Enumerate - индексация при обходе:
for i, letter in enumerate('Это строка. Она тоже последовательность'):
    print(letter, end=f':{i}')

# range генерирует полуоткрытый интервал - начальн.эл. в него входит, конечн. - нет:
for j in range(10):
    print(j)

#print(f'range as is: {range(10)}')

for j in range(11):
    print(j**3)

# Вывести только четные элементы списка:
for n in lst:
    if n % 2 == 0:
        print(n)

# Вывести квадраты четных чисел от 1 до 10:
for j in range(2, 11, 2):
    print(j**2)