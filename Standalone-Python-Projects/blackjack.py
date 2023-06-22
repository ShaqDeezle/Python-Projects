#!/usr/bin/python3

import random
from replit import clear

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def blackjack():

  print(logo)

  ############### Blackjack Project ###############

  ########### Our Blackjack House Rules ###########

  ## The deck is unlimited in size.
  ## There are no jokers.
  ## The Jack/Queen/King all count as 10.
  ## The the Ace can count as 11 or 1.
  ## Use the following list as the deck of cards:
  ## The cards in the list have equal probability of being drawn.
  ## Cards are not removed from the deck as they are drawn.
  ## The computer is the dealer.

  print("""
###################################################  
  Rules:
  
  1. The deck is unlimited in size. 
  2. There are no jokers.
  3. The Jack/Queen/King all count as 10.
  4. The the Ace can count as 11 or 1.
  5. Cards are not removed from the deck as they are drawn.
  6. The computer is the dealer.
  7. BlackJack is 0 (which means 21)!!!:
  
  GoodLuck \U0001F61C
###################################################
  """)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  game_score = {}

  game = True

  def new_game():
    print("\n")
    new_game = input(
      "Would you like to play again? 'Y' for yes, 'N' for no. \n").upper()

    if (new_game == 'Y'):
      clear()
      blackjack()
    else:
      print("\n")
      print("Goodbye")

  def deal_card():
    """
    Function used to pick random card, and assign it to a variable, and then return said variable.
    """
    random_card = random.choice(cards)

    return random_card

  def calculate_score(game_cards):
    """
    Used to calculate total of cards.
    """
    if (sum(game_cards) == 21):
      return 0
    elif (11 in game_cards) and (sum(game_cards) > 21):

      ### this option works also ###

      # new_num = game_cards.index(11)
      # game_cards[new_num] = 1

      #################################

      game_cards.remove(11)
      game_cards.append(1)
      # print(game_cards)
      return sum(game_cards)
    else:
      return sum(game_cards)

  user_cards = []
  computer_cards = []

  for i in range(2):

    random_cards = deal_card()

    user_cards.append(random_cards)

    random_cards = deal_card()
    computer_cards.append(random_cards)

  while game:
    #print(user_cards)
    # print(computer_cards)
    user_total = calculate_score(user_cards)

    computer_total = calculate_score(computer_cards)

    print("\n")
    print(f"Your hand is {user_cards}, so your total amount is {user_total}")
    print(
      f"The computer's hand is {computer_cards}, so the computer's total amount is {computer_total}"
    )
    print("\n")

    if (user_total == 0):
      print("The User Won!!")
      game = False
      new_game()

    elif (user_total > 21):
      print("The User Loses.")
      game = False
      new_game()

    if (computer_total == 0):
      print("The Computer Won!!")
      game = False
      new_game()

    elif (computer_total > 21):
      print("The Computer Loses.")
      game = False
      new_game()

    if (game):
      choice = input(
        "Would you like to draw another card? 'Y' for yes, or 'N' for no. \n"
      ).upper()

      if (choice == 'Y'):
        another_card = deal_card()
        user_cards.append(another_card)

      else:
        game = False

        while (0 < computer_total < 17):
          print("\n")
          print("It's time for the computer to draw a card.")
          another_card = deal_card()
          computer_cards.append(another_card)
          # print(computer_cards)
          computer_total = calculate_score(computer_cards)
          print("\n")
          print(
            f"The computer's hand is {computer_cards}, so the computer's total amount is: {computer_total}"
          )

        if (computer_total == 0):
          print("\n")
          print("The Computer Won!!")
          new_game()
        elif (computer_total > 21):
          print("\n")
          print("The Computer Loses.")
          new_game()
        else:
          game_score["User"] = user_total
          game_score["Computer"] = computer_total
          score = 0
          for key, values in game_score.items():
            if (values > score):
              score = values

          winner = list(game_score.keys())[list(
            game_score.values()).index(score)]

          print("\n")
          print("The winner is " + winner + "!!")
          new_game()


blackjack()
