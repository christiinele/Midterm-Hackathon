"""
This file must contain your main function. This is the file
the repl.it interpreter will execute using the command python game.py.
Christine Le (A01235924)
Alexander Lee (A01236776)
"""

import monster_encounter
import game_map
import doctest


def display_status(character_info):
  """Display character info

  A function which displays the character's info: their name, hp, position, and progress

  :param character_info: a list of the character's information: name, health, coordinates, and current quest progress.
  :precondition: character_info must be a correctly ordered list
  :postcondition: prints character's info in a meaningful way to the user
  """

  for i in range(3):

    if i == 0:

      print(f"\nAdventurer: {character_info[i]}")

    elif i == 1:

      print(f"Current HP: {character_info[i]}/10")

    else:

      print(f"Current Quest Progress: {character_info[4]} of 3 monsters slain. \n")


def health_restoration(current_hp): 
  """Restore health

  A function which restores the player's health. It is used if the character does not encounger a monster upon movement. 

  :param current_hp: the character's current health.
  :precondition: the character's health as a positive integer and if the character has moved a tile without encountering a monster
  :postcondition: restores the character's health by maximum possible amount
  :return: player's updated health
  
  >>> health_restoration(8)
  You've restored two health points! Your current health is at 10.
  10
  >>> health_restoration(10)
  10
  >>> health_restoration(9)
  You've restored one health point! Your current health is at 10.
  10
  >>> health_restoration(3)
  You've restored two health points! Your current health is at 5.
  5
  """

  if current_hp < 9:
    
    current_hp += 2

    print(f"You've restored two health points! Your current health is at {current_hp}.")
  elif current_hp < 10:
    current_hp += 1

    print(f"You've restored one health point! Your current health is at {current_hp}.")

  return current_hp


def post_game_message(character):
  """Give end game message

  A function which prints a message at the end of the adventure.
  
  :param character: a list of the character's information: name, health, position x, position, quest progress
  :precondition: list must be in the proper order: Name, HP, position x, position y, quest progress
  :postcondition: prints end game message
  """

  if character[4] == 3:

    print("\nCongratulations! You have passed the trial, honouring your village's tradition!")

  elif character[4] == 10:

    print("\nThank you for playing, we hope to see you again!")

  else:

    print("\nYou were slain! Game Over!")  


def input_to_int(value):
  """Convert input to an integer

  A function which takes the player input and ensures it is an integer.

  :param value: user input, a number
  :precondition: input is a number
  :postcondition: converts the number from a string to an integer
  :return: value as an integer

  >>> input_to_int("1")
  1
  >>> input_to_int("0")
  Your input was invalid. Please choose from one of the options next time.
  False
  >>> input_to_int("word")
  Your input was invalid. Please choose from one of the options next time.
  False

  """
  
  if value == "1" or value == "2" or value == "3" or value == "4" or value == "5" or value == "6":

      value = int(value)

      return value
  else:

    print("Your input was invalid. Please choose from one of the options next time.")

    return False


def main():
  """Drives the program."""

  # Name, HP, position x, position y, quest progress
  character = ["Bob", 10, 2, 4, 0] 

  print(f"Welcome, aspiring adventurer! Your name is {character[0]} and your village has an unethical rite of passage that requires you to kill three monsters upon turning sixteen. It is do or die, good luck!")

  # The game will continue so long as the character's goal is not met and they are still alive.
  while character[4] < 3 and character[1] >= 1:
    # First iteration prints map with starting coordinates
    game_map.print_game_map(game_map.current_location(character[2], character[3]))
    
    direction = input("Your current position is represented by 'x'. Pick from one of the following options: \n\n 1. North \n 2. East \n 3. South \n 4. West \n 5. Check your status \n 6. Quit game \n\n")

    if input_to_int(direction) != False:

      if input_to_int(direction) == 5:

        display_status(character)

      elif input_to_int(direction) == 6:

        character[4] = 10

      elif game_map.validate_move(input_to_int(direction), character[2], character[3]):

        character[2] = game_map.movement(character, input_to_int(direction))[0]

        character[3] = game_map.movement(character, input_to_int(direction))[1]

        if monster_encounter.find_monster():

          character = monster_encounter.encounter_choice(character)

        else:

          character[1] = health_restoration(character[1])

  post_game_message(character)


if __name__ == "__main__":
    main()

    print("\n")

    doctest.testmod(verbose=True)
    # doctest.testfile('game_map.py', verbose=True) Couldn't get this working?