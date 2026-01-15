import random

class NotImpLementedException(Exception):
    ...

def fich3():
    while True:

        print("Прикорма нет, нужно приманить рыбу живцом!")
        s = input("Сколько времени в минутах нужно привлекать рыбу (0-20)?")
        #if s.isdigit():
        #   print('нужно ввести число!')
        #  continue
        s = int(s)
        win = random.randint(0, 20)
        if s == win:
            print("Зацепила! Тащите к берегу!")
        else:
            print(f"Надо было {win} минут!")
        repeat = input('Попробуете еще раз?')
        if repeat.strip().lower() == 'нет':
            break
def fich1():
    raise NotImpLementedException("Бросай сытный бойл!")

def fich2():
    raise NotImpLementedException("Нужно создать кормящее пылевое пятно с личинками!")

print("Сегодня замечательная погода для улова!")
enter = input("Планируете много поймать (да/нет)?")
#print('да' == enter)
if 'да' == enter:
    print("Отличного улова!")

    choose = input("Какую рыбу вы планируете поймать: карп (1),  лещ (2), щука (3)")

    try:
        if '1' == choose:
            fich1()
        elif '2' == choose:
            fich2()
        elif '3' == choose:
            fich3()


    except NotImpLementedException as err:
        print(f'Рыбы пока нет: {err}')

    print("Значит, просто отдыхайте!")

elif 'нет' == enter:
    print("Значит, просто отдыхайте!")
