while True:

    inp = input('Введите целое число:')

    try:
        inp = int(inp)
        ret = inp ** 3
        print(f'Куб введенного числа равен{ret}')
    except:
        print(f'Нет, все-таки нужно число! Вместо "{inp}"')
    finally:
        print('Еще раз!')