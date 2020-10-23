import rng


def find_monster():
  """Determine whether or not a monster will appear."""  

  if rng.roll_4() == 1:

    return True


def monster_generator():
  """Determine the type of monster.
  
  Randomly selects a type of monster for an encounter

  :return: list of monster's information
  """

  # Monster name, health, attack type
  types_of_monsters = [
    ("goblin", "stabs", [5]),
    ("orc", "punches", [5]),
    ("fairy", "throws a fireball at", [5]),
    ("viper", "bites", [5])]

  monster_type = rng.roll_4()

  if monster_type == 1:

    monster = types_of_monsters[0]

  elif monster_type == 2:

    monster = types_of_monsters[1]

  elif monster_type == 3:

    monster = types_of_monsters[2]
    
  else:
    monster = types_of_monsters[3]

  return monster


def check_initiative():
  """Determine which combatant has initiative.
  
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

  :param character: a list of the character's information: name, health, position x, position, quest progress
  :precondition: list must be in the proper order: Name, HP, position x, position y, quest progress
  :postcondition: gives result of player's choice
  :return: character's health if flee is selected
  """

  monster = monster_generator()
  encounter_choice = ""

  print(f"\nYou've encountered a(n) {monster[0]}!\n")

  while encounter_choice != "1" and encounter_choice != "2":

    encounter_choice = input("Will you: \n\n 1. Fight \n 2. Flee \n\n")

    if encounter_choice == "1" or encounter_choice == "2":

      if encounter_choice == "1":

        character_health = monster_encounter(character_health, monster)

      elif encounter_choice == "2":

        if rng.roll_10() == 1:

          monster_damage = rng.roll_4()
          character_health -= monster_damage
          
          print(f"\nThe {monster[0]} {monster[2]} you for {monster_damage} damage as you were fleeing! Your now have {character_health} health points remaining.")
          
    else:

      print("\nYour input was invalid! Please enter '1' to fight or '2' to flee.")

  return character_health

def player_initiative(character_health, monster):
  """Simulates one turn if player rolls higher initative

  A function which simulates damage taken/received if the player is first to move.
  
  :param character_health: a positive integer, how much health the player currently has
  :param monster: a list of the monster's information: name, health, attack type
  :precondition: health must be positive integers greater than zero
  :postcondition: caculates the amount of damage each combatant takes
  :return: how much health the player is left with
  """

  player_damage = rng.roll_6()
  monster[2][0] -= player_damage
  
  print(f"\nYou gain initiative and strike first! You slice the {monster[0]} for {player_damage} damage!")
  
  if monster[2][0] > 0:
    
    monster_damage = rng.roll_6()
    character_health -= monster_damage
    
    print(f"\nThe {monster[0]} now has {monster[2][0]} health. It {monster[1]} you for {monster_damage} damage! You have {character_health} health points remaining.")

    return character_health
    
  else:

    print(f"\nYou have defeated the {monster[0]}!\n")

    return character_health


def monster_initiative(character_health, monster):
  """Simulates one turn if monster rolls higher initative

  A function which simulates damage taken/received if the monster is first to move.
  
  :param character_health: a positive integer, how much health the player currently has
  :param monster: a list of the monster's information: name, health, attack type
  :precondition: health must be positive integers greater than zero
  :postcondition: caculates the amount of damage each combatant takes
  :return: how much health the player is left with
  """

  monster_damage = rng.roll_6()

  character_health -= monster_damage

  print(f"\nThe {monster[0]} gains initiative! It {monster[1]} you for {monster_damage}. You have {character_health} health points remaining.")

  if character_health <= 0:

      return character_health

  if character_health > 0:

    player_damage = rng.roll_6()
    monster[2][0] -= player_damage
    
    print(f"\nYou brandish your trusty sword and do {player_damage} damage to the {monster[0]}!")
    
    if monster[2][0] < 0:

      print(f"\nYou have defeated the {monster[0]}!")

      return character_health

    else:

      return character_health


def monster_encounter(character, monster):
  """Simulate combat

  A function which simulates combat for however many turns necessary. Uses functions player_initiative and monster_initiative to simulate single turns.

  :param character: a list of the character's information: name, health, position x, position, quest progress
  :param monster: a list of the monster's information: name, health, attack type
  :precondition: lists are appropriately ordered and formatted
  :postcondition: gives result of battle
  :return: character information following the battle
  """

  while character[1] > 0 and monster[2][0] > 0:

    if check_initiative() == 0:
      character[1] = player_initiative(character[1], monster)

    elif check_initiative() == 1:      
      character[1] = monster_initiative(character[1], monster)

    else:
      print("\nIt's a stare down! No one attacks successfully.")

  character[4] += 1

  return character