#Imports random
import random

class Shield:
    def __init__(self):
        #Initializes a new, random Shield
        self.name = random.choice(["Pot Lid", "Wooden Shield", "Reinforced Wooden Shield", "Rusty Iron Shield", 
        "Iron Shield", "Knight's Shield", "Steel Shield"])
        self.defense = random.randint(1,6)
        self.price = random.randint(20, 75)