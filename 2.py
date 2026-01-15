
attempt = 1
while True:
    repeat = input('Забрасываем снова?')

    if repeat == 'нет':
        break

    print(f' Вы ввели {repeat}, Забрасывайте! Попытка', attempt)
    attempt += 1

