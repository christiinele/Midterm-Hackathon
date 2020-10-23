import midterm
import doctest

def initialize_map():
  """Generates a 5 by 5 map.
  
  Creates a map using 5 lists of 5 to show a 5 by 5 grid.

  :return: a 5 by 5 map
  """
  
  map = [["0", "0", "0", "0", "0"], 
  ["0", "0", "0", "0", "0"], 
  ["0", "0", "0", "0", "0"], 
  ["0", "0", "0", "0", "0"], 
  ["0", "0", "0", "0", "0"]]

  return map


def current_location(current_position_x, current_position_y):
  """Assigns player position.
  
  A function which assigns the player, represented by 'x', a position on the map.

  :return: player location on map
  """

  # Clears map
  map = initialize_map()

   # Initializes player position
  map[current_position_y][current_position_x] = "x"

  return map


def print_game_map(map):
  """Displays player on map.

  A function which prints the map with the player's location indicated by 'x'
  """
  print("\n")

  for number in range(len(map)):

    print(map[number])

  print("\n")


def validate_move(direction, current_position_x, current_position_y):
  """Determine whether the player can move in a direction.

  A function which restricts the player's movement to the boundaries of the 5 by 5 map. To be used in combination with function 'movement'.

  :param direction: a positive integer.
  :param current_position_x: a positive integer.
  :param current_position_y: a positive integer.
  :precondition: integer for direction parameter is from 1 to 4, integer for parameters current_position_x and current_position_y is from 0 to 4.
  :postcondition: passes as True or prints statement if not True.
  :return: True or False.

  >>> validate_move(1, 0, 0)
  True
  >>> validate_move(2, 0, 5)
  "\nYou run into a wall! You don't move anywhere."  
  """
  
  if direction == 1:

    if current_position_y != 0:

      return True

    else:

      print("\nYou run into a wall! You don't move anywhere.")

  elif direction == 3:

    if current_position_y != 4:

      return True

    else:

      print("\nYou run into a wall! You don't move anywhere.")  

  elif direction == 2:

    if current_position_x != 4:

      return True

    else:

      print("\nYou run into a wall! You don't move anywhere.")  

  elif direction == 4:

    if current_position_x != 0:

      return True

    else:

      print("\nYou run into a wall! You don't move anywhere.")


def movement(character, direction):
  """Move in a direction
  
  A function which changes the player's position. Either the player's current_position_x or current_position_y is changed, depeding on the direction parameter.

  :param character: a list of the character's information: name, health, position x, position, quest progress
  :param direction: a positive integer
  :preconditon: characater list must be in proper order, direction must be from 1 to 4.
  :postcondition: moves the character
  :return: new position of character
  """

  if direction == 1:  # North

    return character[2], character[3] - 1

  elif direction == 2:  # East

    return character[2] + 1, character[3]

  elif direction == 3:  # South

    return character[2], character[3] + 1

  elif direction == 4:  # West
  
    return character[2] - 1, character[3]