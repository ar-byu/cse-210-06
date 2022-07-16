class GameMaster:
    def __init__(self, dungeon):
        #Initializes a dungeon
        self._dungeon = dungeon

    def start_game(self):
        #Prints flavor text and builds the dungeon
        print("""The king of the land has sent for you, a new knight eager to prove their mettle! He has given you a task; to free a tower on the edge of the kingdom from a 
        dragon, who has taken up residence at the top and claimed it as part of the dragon's hoard. This will not be an easy task, for the tower was enchanted by the court
        wizard several years ago. The levels of the tower are ever changing, so there is no map or guide. You'll have to explore on your own--and pass each trial the tower
        puts forth.
        
        After a week's travel, you finally arrive at the forboding tower. Armed with a satchel full of healing elixirs and a sharp sword, you heave open the
        great entry doors and step inside...""")
        print()
        self._dungeon.build_dungeon()