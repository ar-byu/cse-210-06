#Imports the random module and Actor
import random
from casting.actor import Actor

class Player(Actor):
    #The player's character.
    def __init__(self, name = None):
        #Retrieves a string from player input and constructs Player object.
        if name == None:
            name = input("Please enter your name: ")
        elif not isinstance(name, str):
            raise Exception("Name must be a string")
        super().__init__()
        self._name = name
        self._max_hp = self._hp
        self._base_attack = self._attack
        self._base_max_attack = self._max_attack
        self._defense = 0
        self._gold = 50
        self._weapon = "Short Sword"
        self._shield = "No shield"
        print(f"Greetings, Adventurer! Your name is {self._name}. Your HP is {self._hp} and your attack is {self._attack}.")
        print()

    def reset_attack(self):
        #Resets the attack and max_attack stats to their default base values
        self._attack = self._base_attack
        self._max_attack = self._base_max_attack

    def reset_defense(self):
        #Resets the defense stat to 0
        self._defense = 0

    def check_dead(self):
        #Checks if player HP is zero.
        return self._hp <= 0

    def heal(self):
        #Heals player by a random amount, with a cap of the player's max HP.
        heal_amt = random.randint(15, 20)
        self._hp += heal_amt
        if self._hp > self._max_hp:
            self._hp = self._max_hp
        print(f"You drank an elixir! Your HP is now {self._hp}.")

    def win_scenario(self):
        #calls reset HP and prints flavor text.
        print("The enemy drops some gold. The locked door behind the enemy opens.")
        print()
        self._gold += random.randint(20, 40)
        print("You journey to the next floor...")

    def equip_new_weapon(self, weapon):
        #Adds a weapon's attack to player's base attack and max_attack stats
        self.reset_attack()
        self._attack += weapon.attack
        self._max_attack += weapon.attack
        self._weapon = weapon.name
        return self._attack, self._max_attack
    
    def equip_new_shield(self, shield):
        #Adds a shield's attack to player's base defense stat
        self.reset_defense()
        self._defense += shield.defense
        self._shield = shield.name
        return self._defense

    def pay(self, amount):
        #Subtracts gold from the player's gold
        self._gold -= amount