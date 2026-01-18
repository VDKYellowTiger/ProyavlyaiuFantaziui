from ANIMALS import Animal, Dragon, Bear

if __name__ == '__main__':
    bezzubik = Dragon('Беззубик', 251, eyes_color='золотые!')
    zubastik = Dragon('Зубастик', 108, eyes_color='зеленые!')

    Bear1 = Bear('Саша', 198, 'бурая средняя')

    print(bezzubik)
    print(zubastik)
    bezzubik.eat('рыбу')
    zubastik.eat('овец')
    bezzubik.voice()
    zubastik.voice()

    print(Bear1)
    Bear1.voice()


