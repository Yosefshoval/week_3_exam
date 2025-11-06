# import random
from . import orc


class Goblin(orc.Monster):
    def __init__(self, name, weapon, type='goblin'):
        super().__init__(name, weapon, type)


    def run_away(self): # Bonus
        pass

