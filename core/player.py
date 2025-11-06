import random


class Player:
    def __init__(self, name, profession):
        self.name = name
        self.hp = 50 # start value
        self.speed = random.randint(5, 10) # random 5 - 10
        self.power = random.randint(5, 10) # random 5 - 10. if fighter: + 2
        self.armor_rating = random.randint(5, 15) # random 5 - 15
        self.profession = profession # 'fighter' or 'cure'
        
        if profession == 'fighter':
            self.power += 2
        
        if profession == 'cure':
            self.hp += 10
        

    def speak(self):
        print(f'I am {self.name}. I have been created.')

    def attack(self, monster, hp):
        monster.hp -= hp
        return
