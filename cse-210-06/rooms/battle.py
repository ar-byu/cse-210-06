#Imports GameState class
from directing.game_state import GameState

class Battle:
    def __init__(self, enemy, player):
        #Initalizes an enemy, player, and new GameState
        self._enemy = enemy
        self._player = player
        self._gamestate = GameState()
    
    def _build_battle(self):
        #Retrieves input and calls other functions according to the input.
        print(f"You have encountered a {self._enemy._enemy_type}!")
        while self._gamestate._continue_scenario:
            choice = self._battle_stats_display()
            if choice.lower() == "attack" or choice.lower() == "a":
                self._battle_player_attack()
                if self._gamestate.continue_scenario == False:
                    break
            elif choice.lower() == "heal" or choice.lower() == "h":
                self._player.heal()
            else:
                print("You froze up and couldn't move!")
                print()
            self._battle_enemy_attack()

    def _battle_player_attack(self):
        #Gets a dice roll from the player. If the roll is 1, the player misses. If the roll is 6, the player gets a critical hit.
        # Otherwise, the player attacks with their usual attack. If the enemy dies, ends the fight.
        dice_roll = self._player.roll_dice()
        if dice_roll == 1:
            self._enemy._hp -= 0
            print("Your attack missed!")
        elif dice_roll == 6:
            self._enemy._hp -= self._player._max_attack
            print(f"You made a critical hit! -{self._player._max_attack} to the enemy!")
        else:
            self._enemy._hp -= self._player._attack
            print(f"You attacked! -{self._player._attack} to the enemy!")
        if self._enemy._hp <= 0:
            print("You won!")
            self._player.win_scenario()
            print()
            self._gamestate.continue_scenario = False

    def _battle_enemy_attack(self):
        #Gets a dice roll from the enemy. If the roll is 1, the enemy misses. If the roll is 6, the enemy gets a critical hit.
        # Otherwise, the enemy attacks with their usual attack. If the player dies, ends the game.
        dice_roll = self._enemy.roll_dice()
        if dice_roll == 1:
            self._player._hp -= 0
            print("The enemy's attack missed!")
        elif dice_roll == 6:
            self._player._hp -= (self._enemy._max_attack - self._player._defense)
            print(f"The enemy made a critical hit! You took -{self._enemy._max_attack - self._player._defense} damage!")
        else:
            self._player._hp -= (self._enemy._attack - self._player._defense)
            print(f"Enemy attacked! You took -{self._enemy._attack - self._player._defense} damage!")
        if self._player.check_dead():
            print("You died.")
            self._gamestate.continue_scenario = False
            exit()
        print()

    def _battle_stats_display(self):
    #Retrieves player HP and enemy HP to display. Then retrieves input from the user to return to the build_battle function
        print(f"Your HP: {self._player._hp}")
        print(f"Opponent's HP: {self._enemy._hp}")
        print()
        choice = input("Do you want to [a]ttack or [h]eal? ")
        print()
        return choice