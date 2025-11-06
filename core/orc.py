import random


class Monster:
    def __init__(self, name, weapon, type):
        self.name = name
        self.hp = 50
        self.speed = random.randint(0, 5) # random 0 - 5
        self.power = random.randint(10, 15) # random 10 - 15
        self.armor_rating = random.randint(2, 8) # random 2 - 8
        self.weapon = weapon # Knife | Sword | Axe
        self.type = type

    def speak(self):
        print(f'{self.type} {self.name} is furious!')

    def attack(self):
        pass



class Orc(Monster):
    def __init__(self, name, weapon, type='orc'):
        super().__init__(name, weapon, type)