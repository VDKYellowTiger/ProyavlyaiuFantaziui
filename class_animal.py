from random import choice

class NotImplementedException(Exception):
    pass

class Animal:

    def __init__(self, name, weight, whool=None, eyes_color=None, dimension=None):
        self.name = name
        self.weight = weight  # Килограммы
        self.whool = whool
        self.eyes_color = eyes_color
        self.dimension = dimension

    def __str__(self):
        ret = f'Объект {self.__class__.__name__}: имя={self.name}; вес={self.weight}кг;'
        if self.whool:
            ret += f' шерсть={self.whool}'
        if self.eyes_color:
            ret += f' глаза={self.eyes_color}'
        return ret

    def walk_by_4_legs(self):
        print(f'{self.name} walks:')
        print(f'1 leg')
        print(f'2 leg')
        print(f'3 leg')
        print(f'4 leg')

    def eat(self, food):
        print(f'Животное {self.name} ест {food}')

    def voice(self):
        # pass
        raise NotImplementedException(f'Метод не реализован для общего класса {self.__class__.__name__}')

class Dragon(Animal):
    def voice(self):
        choices = ['рычит', 'кричит' ]
        print(f'Дракон {self.name} {choice(choices)}')

if __name__ == '__main__':
    bezzubik = Dragon('Беззубик', 251, eyes_color='золотые!')
    zubastik = Dragon('Зубастик', 108, eyes_color='зеленые!')

    print(bezzubik)
    print(zubastik)
    bezzubik.eat('рыбу')
    zubastik.eat('овец')
    bezzubik.voice()
    zubastik.voice()

