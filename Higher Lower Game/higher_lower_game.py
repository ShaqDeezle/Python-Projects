#!/usr/bin/python3

import random
import game_data
from replit import clear

def new_game():
  logo = """
      __  ___       __             
     / / / (_)___ _/ /_  ___  _____
    / /_/ / / __ `/ __ \/ _ \/ ___/
   / __  / / /_/ / / / /  __/ /    
  /_/ ///_/\__, /_/ /_/\___/_/     
     / /  /____/_      _____  _____
    / /   / __ \ | /| / / _ \/ ___/
   / /___/ /_/ / |/ |/ /  __/ /    
  /_____/\____/|__/|__/\___/_/     
  """
  
  vs = """
   _    __    
  | |  / /____
  | | / / ___/
  | |/ (__  ) 
  |___/____(_)
  """
  
  print(logo)
  
  game = True
  
  tries = 0
  
  score = 0
  
  game_entries = (len(game_data.data) - 1)
      
  random_choice = random.randint(0, game_entries)

  while game:
    
    if (score > 0) and (tries == 0):
      print(f"\nYou're Right!! Current Score is {score}")
      
    my_dict_1 = game_data.data[random_choice]
  
    print(f"Compare A: {my_dict_1['name']}, a {my_dict_1['description']}, from {my_dict_1['country']}.")
  
    follower_count_a = my_dict_1['follower_count']
    
    print(vs)
  
    random_choice = random.randint(0, game_entries)
  
    my_dict_2 = game_data.data[random_choice]

    while (my_dict_1 == my_dict_2):
      random_choice = random.randint(0, game_entries)
      my_dict_2 = game_data.data[random_choice]

    
    print(f"\nAgainst B: {my_dict_2['name']}, a {my_dict_2['description']}, from {my_dict_2['country']}.")
  
    follower_count_b = my_dict_2['follower_count']
    
    choose = input("\nWho has more followers? Type 'A' or 'B': ")
    
    if (choose == "A"):
      if (follower_count_a > follower_count_b):
        score += 1
        
      elif (follower_count_a < follower_count_b):
        tries += 1
  
    elif (choose == "B"):
      if (follower_count_b > follower_count_a):
        score += 1
        
      elif (follower_count_b < follower_count_a):
        tries += 1
    
    else:
      print("\nPlease choose a proper option between 'A' or 'B'.")
      game = False
      new = input("\nWould you like to restart the game? 'Y' for yes, 'N' for no. ").upper()
      if (new == "Y"):
        clear()
        new_game()
      else:
        print(f"\nGoodbye. Your Final Score was: {score}")
  
    if (tries > 0):
      clear()
      print(logo)
      print(f"Sorry, that's incorrect. Final Score: {score}")
      game = False

new_game()
