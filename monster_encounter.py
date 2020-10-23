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

    monster[0] = "goblin"
    monster[2] = "stabs"

  elif monster_type == 2:

    monster[0] = "orc"
    monster[2] = "punches"

  elif monster_type == 3:

    monster[0] = "fairy"
    monster[2] = "throws a fireball at"
    
  else:
    monster[0] = "viper"
    monster[2] = "bites"

  return monster


def check_initiative():
  monster_initiative = rng.roll_20()
  character_initiative = rng.roll_20()

  if character_initiative > monster_initiative:

    return 0

  elif monster_initiative > character_initiative:

    return 1


def encounter_choice(character_health):
  monster = monster_generator()
  encounter_choice = ""

  print(f"\nYou've encountered a(n) {monster[0]}!\n")

  while encounter_choice != 1 and encounter_choice != 2:
    encounter_choice = input("Will you: \n\n 1. fight \n 2. flee \n\n")

    if encounter_choice == "1" or encounter_choice == "2":
      encounter_choice = int(encounter_choice)

      if encounter_choice == 1:
        character_health = monster_encounter(character_health, monster)
      elif encounter_choice == 2:
        if rng.roll_10() == 1:
          monster_damage = rng.roll_4()
          character_health -= monster_damage
          
          print(f"\nThe {monster[0]} {monster[2]} you for {monster_damage} damage as you were fleeing! Your HP is now {character_health}.")
          
    else:
      print("\nYour input was invalid! Please enter '1' to fight or '2' to flee.")

  return character_health

def player_initiative(character_health, monster):
  player_damage = rng.roll_6()
  monster[1] -= player_damage
  
  print(f"\nYou gain initiaive and strike first! You slice the {monster[0]} for {player_damage} damage!")
  
  if monster[1] > 0:
    
    monster_damage = rng.roll_6()
    character_health -= monster_damage
    
    print(f"\nThe {monster[0]} now has {monster[1]} health. It {monster[2]} you for {monster_damage} damage! You have {character_health} health left.")

    return character_health
    
  else:
    print(f"\nYou have defeated the {monster[0]}!\n")

    return character_health


def monster_initiative(character_health, monster):
  monster_damage = rng.roll_6()

  character_health -= monster_damage

  print(f"\nThe {monster[0]} gains initiative! It {monster[2]} you for {monster_damage}. You have {character_health} health left.")

  if character_health <= 0:
      return character_health

  if character_health > 0:
    player_damage = rng.roll_6()
    monster[1] -= player_damage
    
    print(f"\nYou brandish your trusty sword and do {player_damage} damage to the {monster[0]}!")
    
    if monster[1] < 0:
      print(f"\nYou have defeated the {monster[0]}!")

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
      print("\nIt's a stare down! No one attacks successfully.")

  character[4] += 1

  return character