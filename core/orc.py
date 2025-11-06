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
    
    def plus_power(self, weapon, power):
        if weapon == 'knife':
            power *= 0.5
        elif weapon == 'sword':
            power == power
        elif weapon == 'axe':
            power *= 1.5
        return power




    def attack(self, player, hp):
        hp = self.plus_power(self.weapon, hp)
        player.hp -= hp
        return



class Orc(Monster):
    def __init__(self, name, weapon, type='orc'):
        super().__init__(name, weapon, type)