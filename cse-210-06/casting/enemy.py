#Imports random, EnemyMaster, and Actor
import random
from directing.enemy_master import EnemyMaster
from casting.actor import Actor

class Enemy(Actor):
    #An actor type that is not controlled by the player
    def __init__(self):
        #Gets enemy options and randomly generates an enemy and its associated stats
        super().__init__()
        enemy_options = EnemyMaster()
        self._enemy_type = random.choice(enemy_options._enemy_list)