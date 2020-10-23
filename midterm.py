"""
This file must contain your main function. This is the file
the repl.it interpreter will execute using the command python game.py.
Christine Le (A01235924)
Alexander Lee (A01236776)
"""


import monster_encounter
import game_map


def main():
  """Drives the program."""

  print("Welcome, aspiring adventurer! Your village has an unethical rite of passage that requires you to kill three monsters upon turning sixteen. It is do or die, good luck! \n \n")

  # Name, HP, position x, position y, quest progress
  character = ["Bob", 10, 2, 4, 0]  

  game_map.print_game_map(game_map.current_location(character[2], character[3]))

  direction = int(input("Your current position is represented by 'x'. Pick from one of the following options: 1. north, 2. east, 3. south, 4. west, 5. check your current status, 6. quit game. "))

  if game_map.validate_move(direction, character[2], character[3]):
    character[2] = game_map.movement(character, direction)[0]
    character[3] = game_map.movement(character, direction)[1]

    game_map.print_game_map(game_map.current_location(character[2], character[3]))


if __name__ == "__main__":
    main()
