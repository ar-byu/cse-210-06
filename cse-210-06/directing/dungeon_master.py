#Imports random and necessary classes
import random
from casting.enemy import Enemy
from casting.boss import Boss
from directing.riddle_master import RiddleMaster
from rooms.shop import Shop
from rooms.battle import Battle
from rooms.puzzle import PuzzleRoom

class DungeonMaster:
    def __init__(self, player):
        #Initializes the assets necessary to build a Dungeon
        self._player = player
        self._riddle_list = RiddleMaster()
        self._levels = random.randint(8, 12)
        self._boss = Boss()
        
    def build_dungeon(self):
        #Displays player's stats and gets a room choice for each level in the dungeon. Once the levels are complete, creates a boss battle.
        for level in range(self._levels):
            print(f"{self._player._name} | HP: {self._player._hp} | ATK: {self._player._attack} | DEF: {self._player._defense} | GOLD: {self._player._gold}")
            print(f"EQUIPMENT: {self._player._weapon} | {self._player._shield}")
            print()
            self._choose_room()
            self._floor_type()
        self._choose_room()
        boss_battle = Battle(self._boss, self._player)
        boss_battle._build_battle()
        self._outro()

    def _choose_room(self):
        #Allows the player to choose which room to enter. Calls the appropriate room, or heals the player if that option is chosen.
        choice = input("""You enter a short hallway. On the right is a sign with the word 'shop' painted on it. 
            On the left is a blank door. Do you go into the [s]hop, or [c]ontinue up the tower? You could also [h]eal if you need to. """)
        print()
        if choice.lower() == "s" or choice.lower == "shop":
            shop = Shop(self._player)
            shop.enter_shop()
            print(f"{self._player._name} | HP: {self._player._hp} | ATK: {self._player._attack} | DEF: {self._player._defense} | GOLD: {self._player._gold}")
            print(f"EQUIPMENT: {self._player._weapon} | {self._player._shield}")
            print()
            print("You leave the shop and open the blank door.")
            print()
        elif choice.lower() == "c" or choice.lower == "continue":
            print("You ignore the shop and continue to the next room.")
            print()
        elif choice.lower() == "h" or choice.lower == "heal":
            self._player.heal()
            print("Feeling refreshed, you continue to the next room.")
            print()

    def _floor_type(self):
        #Determines what type of floor the level should be, and calls a new room accordingly.
        floor_type = random.choice(["battle", "puzzle"])
        if floor_type == "battle":
            enemy = Enemy()
            battle = Battle(enemy, self._player)
            battle._build_battle()
        elif floor_type == "puzzle":
            puzzle_room = PuzzleRoom()
            puzzle_room._build_puzzle()
        else:
            print("""So, I've been thinking. When life gives you lemons, don't make lemonade. Make life take the lemons back! I don't want your lemons, what am I
            supposed to do with these?! Demand to see life's manager! Make life rue the day it thought it could give Cave Johnson lemons. Do you know who I am?
            I'm the man who's going to burn your house down! With the lemons! I'm gonna get my engineers to invent a combustible lemon that burns your house down!""")
            exit()

    def outro():
    #Prints flavor text.
        print("""Well done, Adventurer! The dragon, now slain, falls off the tower with a mighty crash. The wizard's tower is finally freed from the dragon's greed.
    The court wizard can finally return to their residence and bless the realm once more. Pleased with  your efforts, the king awards you with a large sum of gold,
    and promises to call on you if ever there is need in the future.""")