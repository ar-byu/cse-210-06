#Imports the random module
import random

class Actor:
    #A person or object in a production.
    def __init__(self):
        #Initializes the actor's stats
        self._hp = random.randint(50, 75)
        self._attack = random.randint(5, 10)
        self._max_attack = self._attack * 3

    def roll_dice(self):
        #Retrieves a random number based on a six sided die
        dice = random.randint(1, 6)
        if dice == 1:
            return 0
        elif dice == 6:
            return 6
        else:
            return dice