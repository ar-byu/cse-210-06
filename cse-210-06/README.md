# Tower Climber
"Have patience. Go where you must go, and hope!" ~ Gandalf, The Two Towers

## Getting Started
---
Make sure you have Python 3.8 or newer installed. This game does not require any extra libraries to run. Once you have downloaded all modules for the game, you can run the program from a terminal using a command like this:
```
python3 __main__.py
```
If this doesn't work, make sure you're in the correct directory.

This game can also be run from an IDE such as Visual Studio Code. Select the "main.py" file and press the Run button.

### How to Play
---
Start by entering your name, or the name you want your adventurer to be called. After that, you can choose how to proceed by entering the letter enclosed in square brackets.

The game will choose a random number of "floors" for you to traverse. Each floor can either be a battle or a riddle. For battles, the player can either attack or heal. For puzzles, the player must enter the correct answer (there are two different variations on the answer) in order to continue.

After each floor has been beaten, there will be a boss battle. This battle is designed to be longer and a bit more strategic, so it's recommended that you don't simply spam "Attack".

The game ends either when the player's HP reaches 0, or the boss is defeated.

## Project Structure
---
This project is structured as follows:
```
casting             (cast objects for the game)
directing           (various orchestrators)
rooms               (rooms that can be encountered)
__main__.py         (the main access point for the game)
README.md           (general information)
```
## Required Technologies
---
* Python 3.8.0 or newer

## Authors
---
Anna Rector, CSE 210 student. lighteternal.lunae@gmail.com, arector2002@gmail.com

_**It should be noted that the source code used for this game was a pre-existing project from the author. Both the source code and this version's code were hand-written by the author.**_