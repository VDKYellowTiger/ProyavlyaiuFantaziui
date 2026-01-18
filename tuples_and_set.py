# Кортежи и множества

crt_red = (255, 0, 0)
crt_green = (0, 255, 0)
crt_blue = (0, 0, 255)

print(crt_red[0])

colors = {
    crt_red: 'Красный цвет',
    crt_green: 'Зеленый цвет',
    crt_blue: 'Синий цвет',
}

print(colors)

s1 = {1, 2, 2, 3, 3, 4}

s2 = {3, 4,4,4,4,5}

print(s1 & s2)