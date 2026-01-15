while True:

    inp = input('Введите целое число:')

    try:
        numerator = 1111
        inp = int(inp)
        ret = numerator / inp
        print(f'{numerator} делить на {inp} равно {ret}')

    except ValueError as error:
        print(f'Нет, все-таки нужно число! Вместо "{inp}" получено исключение {type(error)}')
    except ZeroDivisionError as error:
        print(f'Ошибка деления на ноль ({type(error)}): {error}')
    except Exception as error:
        print(f'Другая ошибка({type(error)}): {error}')

    finally:
        print('Еще раз!')