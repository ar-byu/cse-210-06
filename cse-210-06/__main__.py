# Imports classes from files
from casting.player import Player
from directing.dungeon_master import DungeonMaster
from directing.game_master import GameMaster


#Defines main
def main():
    #Welcomes the player. Initializes a Player, a DungeonMaster, and a GameMaster. Calls start_game to begin the game.
    print("""Welcome to Tower Climber, a short and completely randomized dungeon crawler game!""")
    print()
    player = Player()
    dungeon = DungeonMaster(player)
    director = GameMaster(dungeon)
    director.start_game()

#Starts the game
if __name__ == "__main__":
    main()