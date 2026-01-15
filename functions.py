
def circle_square(radius):
    sq = radius * radius * 3.1415926
    return sq

def reatangle_square(a, b):
    return a * b

def fac1(n):
    ret = 1
    while n > 1:
        ret *= n
        n -= 1
    return ret

def fac_r(n):
    if n < 2:
        return 1
    return n * fac_r(n - 1)



s1 = circle_square(10)
print(f'Площадь круга радиусом 10 равна {s1}')

s2 = circle_square(radius=15)
print(f'Площадь круга радиусом 15 равна {s2}')

s3 = circle_square(radius=23)
print(f'Площадь круга радиусом 23 равна {s3}')


r1 = reatangle_square(10, 12)
print(f'Площадь прямоугольника со сторонами 10, 12 равна {r1}')

r2 = reatangle_square(100, 122)
print(f'Площадь прямоугольника со сторонами 10, 12 равна {r2}')


n = 0
f1 = fac_r(n)
print(f'Факториал числа {n} равен {f1}')

n = 1
f1 = fac_r(n)
print(f'Факториал числа {n} равен {f1}')

n = 3
f1 = fac_r(n)
print(f'Факториал числа {n} равен {f1}')

n = 5
f1 = fac_r(n)
print(f'Факториал числа {n} равен {f1}')

n = 6
f1 = fac_r(n)
print(f'Факториал числа {n} равен {f1}')