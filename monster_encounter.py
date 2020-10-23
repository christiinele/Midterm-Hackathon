import rng


def find_monster():
  """Determine whether or not a monster will appear"""  
  if rng.roll_4() == 1:
    return True


def monster_generator():
  """Determine the type of monster"""
  monster = ["", 5, ""]
  monster_type = rng.roll_4()

  if monster_type == 1:

    monster[0] = "Goblin"
    monster[2] = "stabs"

  elif monster_type == 2:

    monster[0] = "Orc"
    monster[2] = "punches"

  elif monster_type == 3:

    monster[0] = "Fairy"
    monster[2] = "throws a fireball at"
    
  else:
    monster[0] = "Viper"
    monster[2] = "bites"

  return monster


def check_initiative():
  """Determine which combatant has initiative
  
  A function which simulates two individual dice rolls of a 20-sided die, one for the player and one for the monster.
  
  :return: a value indicative of who has initiative
  """
  monster_initiative = rng.roll_20()
  character_initiative = rng.roll_20()

  if character_initiative > monster_initiative:

    return 0

  elif monster_initiative > character_initiative:

    return 1


def encounter_choice(character_health):
  """Select whether to fight or flee from the monster
  
  When encountering a monster, the player can choose to either fight it or flee from it. This function is where the player provides that choice.

  :param character: A list of the character's stats
  :precondition: list must be in the proper order: Name, HP, position x, position y, quest progress
  :postcondition: gives result of player's choice
  """
  monster = monster_generator()
  encounter_choice = ""

  print(f"You've encountered a(n) {monster[0]}!")

  while encounter_choice != "fight" and encounter_choice != "flee":
    encounter_choice = input("Will you fight or flee? ").lower().strip()

    if encounter_choice == "fight":
      character_health = monster_encounter(character_health, monster)
    elif encounter_choice == "flee":
      if rng.roll_10() == 1:
        monster_damage = rng.roll_4()
        character_health -= monster_damage
        
        print(f"The {monster[0]} stabbed you in the back for {monster_damage} as you were fleeing! Your HP is now {character_health}.")
    else:
      print("Your input was invalid! Please enter fight or flee.")

  return character_health