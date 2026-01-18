from .animal import Animal
from random import choice

class Bear(Animal):
    def voice(self):
        choices = ['рычит', 'пыхтит', 'орет' ]
        print(f'Bear {self.name} {choice(choices)}')

