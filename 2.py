

repeat = input('Забрасываем снова?')

attempt = 1
while repeat.lower() != 'нет':
    print('Забрасывайте! Попытка', attempt)
    attempt += 1
    repeat = input('Забрасываем снова?')