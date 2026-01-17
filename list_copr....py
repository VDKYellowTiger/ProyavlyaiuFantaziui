#Нужны квадраты всех нечет.чисел из этого списка, тоже в виде списка:
#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Рабочая, но тяжелая конструкция:
#lst2 = []
#for d in lst:
#    if d % 2 != 0:
#        lst2.append(d**2)
#print(f'{lst2=}')

#То же самое, но короче из-за списочного включения:
#lst2_1 = [k**2 for k in lst if k % 2 != 0]
#print(f'{lst2_1=}')

#lst = [k for k in range(1, 100 + 1)]

#print(f'{lst=}')

string = 'А роза упала на лапу Азора'

def is_palindrome(string: str) -> bool:
    spaceless1 = [k.upper() for k in string if k != ' ']
    spaceless2 = [k.upper() for k in string if k != ' ']
    spaceless2.reverse()

    return spaceless1 == spaceless2

def is_palindrome2(string: str) -> bool:
    spaceless1 = [k.upper() for k in string if k != ' ']

    for i in range(-1, -1 * len(spaceless1)-1, -1):
        reverse_i = (-1 * i) - 1
        if spaceless1[i] != spaceless1[reverse_i]:
            return False
    return True

ret = is_palindrome2(string)

print(ret)

