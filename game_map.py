def initialize_map():
  map = [["0", "0", "0", "0", "0"], 
  ["0", "0", "0", "0", "0"], 
  ["0", "0", "0", "0", "0"], 
  ["0", "0", "0", "0", "0"], 
  ["0", "0", "0", "0", "0"]]

  return map


def game_map(current_position_x, current_position_y):

  # Clears map
  map = initialize_map()

   # Initializes player position
  map[current_position_y][current_position_x] = "x"

  return map


def print_game_map(map):
  for i in range(len(map)):
    print(map[i])

  print("\n")


print_game_map(game_map(2, 4))