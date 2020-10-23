def initialize_map():
  map = [["0", "0", "0", "0", "0"], 
  ["0", "0", "0", "0", "0"], 
  ["0", "0", "0", "0", "0"], 
  ["0", "0", "0", "0", "0"], 
  ["0", "0", "0", "0", "0"]]

  return map


def current_location(current_position_x, current_position_y):

  # Clears map
  map = initialize_map()

   # Initializes player position
  map[current_position_y][current_position_x] = "x"

  return map


def print_game_map(map):
  for i in range(len(map)):
    print(map[i])

  print("\n")


def validate_move(direction, current_position_x, current_position_y):
  """
  do doctests for this one
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
  else:
    print("\nYour input was invalid. Please choose from one of the options listed next time.")


def movement(character, direction):
  if direction == 1:  # North
    return character[2], character[3] - 1
  elif direction == 2:  # East
    return character[2] + 1, character[3]
  elif direction == 3:  # South
    return character[2], character[3] + 1
  elif direction == 4:  # West
    return character[2] - 1, character[3]