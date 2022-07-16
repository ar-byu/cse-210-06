#Imports random and Enemy
import random
from casting.enemy import Enemy

class Boss(Enemy):
    def __init__(self):
        #Initializes boss stats
        self._enemy_type = "red dragon"
        self._hp = random.randint(90, 110)
        self._attack = random.randint(8, 12)
        self._max_attack = random.randint(15, 20)