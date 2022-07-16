#Imports random
import random

class Weapon:
    def __init__(self):
        #Initializes a new, random Weapon object
        self.name = random.choice(["Spear", "Mace", "Hand Axe", "Dagger", "Fire", "Ice", "Thunder"])
        self.attack = random.randint(1,6)
        self.price = random.randint(20, 75)