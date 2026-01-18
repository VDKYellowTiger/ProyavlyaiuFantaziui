from .animal import Animal
from random import choice

class Dragon(Animal):
    def voice(self):
        choices = ['рычит', 'кричит' ]
        print(f'Дракон {self.name} {choice(choices)}')