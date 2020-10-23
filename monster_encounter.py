import rng


def find_monster():
  """Determine whether or not a monster will appear"""  
  if rng.roll_4() == 1:
    return True


def monster_generator():
  """Determine the type of monster"""
  monster = ["", 5, ""]  # monster name, health, attack type
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
        
        print(f"The {monster[0]} {monster[2]} you in the back for {monster_damage} damage as you were fleeing! Your HP is now {character_health}.")
    else:
      print("Your input was invalid! Please enter fight or flee.")

  return character_health

def player_initiative(character_health, monster):
  """Simulates one turn if player rolls higher initative

  A function which simulates damage taken/received if the player is first to move.
  
  :param character_health: 
  :param monster:
  """
  player_damage = rng.roll_6()
  monster[1] -= player_damage
  
  print(f"You gain initiaive and strike first! You slice the {monster[0]} for {player_damage} damage!")
  
  if monster[1] > 0:
    
    monster_damage = rng.roll_6()
    character_health -= monster_damage
    
    print(f"The {monster[0]} now has {monster[1]} health. It {monster[2]} you for {monster_damage} damage! You have {character_health} health left.")

    return character_health
    
  else:
    print(f"You have defeated the {monster[0]}!")

    return character_health


def monster_initiative(character_health, monster):
  monster_damage = rng.roll_6()

  character_health -= monster_damage

  print(f"The {monster[0]} gains initiative! It {monster[2]} you for {monster_damage}. You have {character_health} health left.")

  if character_health <= 0:
      return character_health

  if character_health > 0:
    player_damage = rng.roll_6()
    monster[1] -= player_damage
    
    print(f"You brandish your trusty sword and do {player_damage} damage to the {monster[0]}!")
    
    if monster[1] < 0:
      print(f"You have defeated the {monster[0]}!")

      return character_health

    else:

      return character_health


def monster_encounter(character, monster):
  while character[1] > 0 and monster[1] > 0:

    if check_initiative() == 0:
      character[1] = player_initiative(character[1], monster)

    elif check_initiative() == 1:      
      character[1] = monster_initiative(character[1], monster)

    else:
      print("It's a stare down! No one attacks successfully.")

  character[4] += 1

  return character