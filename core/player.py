import random


class Player:
    def __init__(self, name, speed, power, armor_rating, profession):
        self.name = name
        self.hp = 50 # start value
        self.speed = speed # random 5 - 10
        self.power = power # random 5 - 10. if fighter: + 2
        self.armor_rayig = armor_rating # random 5 - 15
        self.profession = profession # 'fighter' or 'cure'


    def speak(self):
        print(f'I am {self.name}.')

    def attack(self):
        pass



p1 = Player('Yosef', 8, 7, 12, 'fighter')
p1.speak()