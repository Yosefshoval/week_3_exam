import random
# import core.orc
# import core.goblin
from core import orc, goblin, player



class Game:

    def start(self):
        option = self.show_menu()
        if option.lower() == 'b':
            player = self.create_player()
            monster = self.choose_random_monster()
            # players = [player, monster]
            
            result = self.battle(player, monster)
            self.start()

        if option.lower() == 'e':
            return


    def show_menu(self):
        option = input('Choose "b" for Battle, or "e" to Exit: ')
        while option.lower() != 'b' or option.lower() != 'e':
            option = input('Try again please: ')
        return option
        


    def create_player(self, name):
        profession = random.choice(['fighter', 'cure'])
        return player.Player(name, profession)
        

    def choose_random_monster(self, name, weapon):
        monsters = [orc.Orc, goblin.Goblin]
        monster = random.choice(monsters)
        monster = monster(name, weapon)
        return monster


    def battle(self, player, monster):
        
        player_s = self.roll_dice(6)
        monster_s = self.roll_dice(6)

        validity = monster if monster.speed + monster_s > player.speed  + player_s else player
        attacked = monster if validity == player else player
        
        while validity.hp > 0 and attacked.hp > 0:

            add_to_speed = self.roll_dice(20)

            if add_to_speed + validity.speed > attacked.armor_rating:
                validity.attack()  #!
                
                bull = self.roll_dice(6)
                bull += validity.power

                validity.attack(attacked, bull)
            
            attacked, validity = validity, attacked


    def roll_dice(self, sides):
        return random.randint(1, sides)
