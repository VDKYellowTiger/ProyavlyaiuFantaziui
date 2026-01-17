#Списки:

lst = [1, 3, 4, 2, 0, 123, 321, 222]

print(lst)


#Добавление списка
lst.append(1111)
lst.append(3_333)

print(lst)

lst2 = ['first', 'second', 'third']

#Расширение списка:
#lst.extend(lst2)

# lst = lst2

print(lst)

#Сортировка. Метод ничего не возвращает:
lst.sort(key=lambda x: len(str(x)))
lst.sort()
print(f'sorted={lst}')

lst.reverse()

print(f'reverse={lst}')

last = lst.pop()

print(f'last element={last}, list after second pop={lst}')

first = lst.pop(0)

print(f'first element={first}, list after second pop={lst}')

print(321 in lst, 555 in lst)