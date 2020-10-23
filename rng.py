import random


def roll_4():
  """Roll 4-sided die
    
  :return: result of roll"""
  return random.randint(1, 4)


def roll_6():
  """Roll 6-sided die
    
  :return: result of roll"""
  return random.randint(1, 6)


def roll_10():
  """Roll 10-sided die

  :return: result of roll"""
  return random.randint(1, 10)


def roll_20():
  """Roll 20-sided die
  
  :return: result of roll
  """
  return random.randint(1, 20)