import random
import time
# import core.orc
# import core.goblin
from core import orc, goblin, player



class Game:

    def start(self):
        
        option = self.show_menu()
        
        if option.lower() == 'b':
            player = self.create_player(input('Enter your name: '))
            monster = self.choose_random_monster(input('Choose a name for the monster: '), random.choice(['knife', 'sword', 'axe']))
            
            player_s = self.roll_dice(6)
            monster_s = self.roll_dice(6)

            attacker = monster if monster.speed + monster_s > player.speed + player_s else player
            attacked = monster if attacker == player else player
            print(f'{attacker.name} is the first player!')

            self.battle(attacker, attacked)
            self.end_print(player, monster)
            
            self.start()

        if option.lower() == 'e':
            return


    def show_menu(self):
        option = input('\nChoose "b" for Battle, or "e" to Exit: ')
        while option.lower() != 'b' and option.lower() != 'e':
            option = input('Try again please: ')
        return option
        


    def create_player(self, name):
        profession = random.choice(['fighter', 'cure'])
        p = player.Player(name, profession)
        p.speak()
        return p
        
    def choose_random_monster(self, name, weapon):
        monsters = [orc.Orc, goblin.Goblin]
        monster = random.choice(monsters)
        monster = monster(name, weapon)
        monster.speak()
        return monster


    def end_print(self, player, monster):
        """ print the rating of each player and the winner """

        print(f'moster: hp: {monster.hp}. speed: {monster.speed}. armor_rating: {monster.armor_rating}. weapon: {monster.weapon}.')
        print(f'player: hp: {player.hp}. speed: {player.speed}. armor_rating: {player.armor_rating}. profession: {player.profession}.')
        winner = monster if monster.hp > player.hp else player
        print(f'The winner in this game is.... : {winner.name}!!!')
        print('The game ended.\n')
        return
    

    def battle(self, attacker, attacked):
        
        while attacker.hp > 0 and attacked.hp > 0:
            print(f'Now the current attacker is {attacker.name}!')
            print(f'{attacker.name} has {attacker.hp} hp. {attacked.name} has {attacked.hp}\n')
            
            time.sleep(1.5)

            add_to_speed = self.roll_dice(20)
            print(f'Rolling: {add_to_speed}')
            time.sleep(0.5)

            if add_to_speed + attacker.speed > attacked.armor_rating:
                print('There is a injury!!\n')
                
                bull = self.roll_dice(6)
                bull += attacker.power

                attacker.attack(attacked, bull)

            else:
                print('Miss...\n')
            
            attacked, attacker = attacker, attacked
        
        return



    def roll_dice(self, sides):
        return random.randint(1, sides)
