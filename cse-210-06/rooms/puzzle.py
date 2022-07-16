#Imports classes from other files
from directing.riddle_master import RiddleMaster
from directing.game_state import GameState

class PuzzleRoom:
    def __init__(self):
        #Initializes a new RiddleMaster and GameState
        self._riddle_list = RiddleMaster()
        self._gamestate = GameState()

    def _build_puzzle(self):
        #Retrieves a random riddle from riddle_list, and verifies that the answer given via present_riddle matches the answers in the riddle
        riddle = self._riddle_list.get_riddle()
        print("You enter a wide open room...")
        print()
        while self._gamestate.continue_scenario:
            answer = self._present_riddle(riddle).lower()
            if answer == riddle[2].lower() or answer == riddle[3].lower():
                self._riddle_win()
            else:
                self._riddle_lose()

    def _riddle_lose(self):
        #Prints flavor text
        print("That was incorrect. Try again!")
        print()

    def _present_riddle(self, riddle):
        #Retrieves the riddle from build_puzzle and displays it and its hint, then gets input from the player. Returns input to build_puzzle.
        print(riddle[0])
        print()
        print(f"Hint: {riddle[1]}")
        answer = input("What will you write? ")
        print()
        return answer

    def _riddle_win(self):
        #Prnts flavor text. Sets gameState's continue_scenario to false.
        print("The door glows with magical energy and swings open as soon as you put the quill down. You leave the room and climb the next set of stairs...")
        self._gamestate.continue_scenario = False