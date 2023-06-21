#!/usr/bin/python3

#Number Guessing Game Objectives:

import random
from replit import clear

logo = """

╭━╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮
┃┃╰╮┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃
┃╭╮╰╯┣╮╭┳╮╭┫╰━┳━━┳━╮┃┃╱╰╋╮╭┳━━┳━━┳━━┳┳━╮╭━━╮┃┃╱╰╋━━┳╮╭┳━━╮
┃┃╰╮┃┃┃┃┃╰╯┃╭╮┃┃━┫╭╯┃┃╭━┫┃┃┃┃━┫━━┫━━╋┫╭╮┫╭╮┃┃┃╭━┫╭╮┃╰╯┃┃━┫
┃┃╱┃┃┃╰╯┃┃┃┃╰╯┃┃━┫┃╱┃╰┻━┃╰╯┃┃━╋━━┣━━┃┃┃┃┃╰╯┃┃╰┻━┃╭╮┃┃┃┃┃━┫
╰╯╱╰━┻━━┻┻┻┻━━┻━━┻╯╱╰━━━┻━━┻━━┻━━┻━━┻┻╯╰┻━╮┃╰━━━┻╯╰┻┻┻┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
"""

print(logo)


def number_guessing_game():
  number = []
  game = True

  # number = randint(1, 100)

  for i in range(1, 101):
    number.append(i)

  while (game):
    random_number = random.choice(number)

    game_rules = input(
      "I'm thinking of a number between 1 and 100. \nChoose a difficulty. Type 'easy' or 'hard': "
    )

    if (game_rules == 'easy'):
      tries = 10
    elif (game_rules == 'hard'):
      tries = 5
    else:
      print("\n")
      print("You didn't choose a correct game mode. Game is Over.")
      tries = 0
      game = False

    while (tries > 0) and (game):
      print("\n")
      guess = int(input("What's your guess between 1 and 100? \n"))
      if (guess < 1):
        tries -= 1
        print("\n")
        print(f"Your guess was not in range, you have {tries} tries left.")

      elif (guess > 100):
        tries -= 1
        print("\n")
        print(f"Your guess was not in range, you have {tries} tries left.")

      elif (guess != random_number) and (0 < guess < 101):
        tries -= 1

        if (guess < random_number):
          print("\n")
          print(
            f"Your guess is too low, try again. You have {tries} tries left.")
        elif (guess > random_number):
          print("\n")
          print(
            f"Your guess is too high, try again. You have {tries} tries left.")

        if (tries == 0):
          print("\n")
          print(
            f"You have {tries} tries left. The answer was {random_number}. Game Over."
          )
          game = False

      else:
        game = False
        if (tries == 1):
          print("\n")
          print(
            f"You Won! You guessed the correct answer, which was {random_number}, and you had {tries} try left. Great Job!!"
          )
        else:
          print("\n")
          print(
            f"You Won! You guessed the correct answer, which was {random_number}, and you had {tries} tries left. Great Job!!"
          )

  print("\n")
  new_game = input(
    "Would you like to play again? 'y' for yes, or 'n' for no. \n").lower()
  if (new_game == 'y'):
    clear()
    number_guessing_game()
  else:
    print("\n")
    print("Goodbye.")
    game = False


number_guessing_game()
