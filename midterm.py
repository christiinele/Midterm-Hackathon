"""
This file must contain your main function. This is the file
the repl.it interpreter will execute using the command python game.py.
Christine Le (A01235924)
Alexander Lee (A01236776)
"""


import monster_encounter
import game_map


def display_status(character_info):
  for i in range(3):
    if i == 0:
      print(f"\nAdventurer: {character_info[i]}")
    elif i == 1:
      print(f"Current HP: {character_info[i]}/10")
    else:
      print(f"Current Quest Progress: {character_info[4]} of 3 monsters slain. \n")


def health_restoration(current_hp): 

  if current_hp < 9:
    current_hp += 2

    print("\nYou've restored two health points!\n")
  elif current_hp < 10:
    current_hp += 1

    print("\nYou've restored one health point!\n")

  return current_hp      


def main():
  """Drives the program."""

  print("Welcome, aspiring adventurer! Your village has an unethical rite of passage that requires you to kill three monsters upon turning sixteen. It is do or die, good luck!")

  # Name, HP, position x, position y, quest progress
  character = ["Bob", 10, 2, 4, 0] 

  # The game will continue so long as the character's goal is not met and they are still alive.
  while character[4] < 3 and character[1] >= 1:
    # First iteration prints map with starting coordinates
    game_map.print_game_map(game_map.current_location(character[2], character[3]))
    
    direction = input("Your current position is represented by 'x'. Pick from one of the following options: \n\n 1. North \n 2. East \n 3. South \n 4. West \n 5. Check your status \n 6. Quit game. \n\n")

    if direction == "1" or direction == "2" or direction == "3" or direction == "4" or direction == "5" or direction == "6":
      direction = int(direction)

      if direction == 5:
        display_status(character)
      elif direction == 6:
        character[4] = 10
      elif game_map.validate_move(direction, character[2], character[3]):
        character[2] = game_map.movement(character, direction)[0]
        character[3] = game_map.movement(character, direction)[1]

        if monster_encounter.find_monster():
          character = monster_encounter.encounter_choice(character)
        else:
          character[1] = health_restoration(character[1])

    else:
      print("\nYour input was invalid. Please choose from one of the options next time.\n")


if __name__ == "__main__":
    main()
