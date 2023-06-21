#!/usr/bin/python3

import random

word_list = ["aardvark", "baboon", "camel"]

stages = [
  '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

chosen_word = random.choice(word_list)

count_of_chosen_word = len(chosen_word)

lives = 6

display = []

game = True

previous_guesses = []

for i in range(count_of_chosen_word):
  display.append("_")

print(chosen_word)

while (game):

  print(display)

  print("\n")
  guess = input("Guess a Letter ").lower()
  print("\n")

  for i in range(count_of_chosen_word):
    if (guess == chosen_word[i]):
      display[i] = guess

      if ("_" not in display):
        print("You Win!!")
        print(f"The word you were looking for is '{''.join(display)}'")
        game = False

  if (guess in previous_guesses):
    print(f"This letter, '{guess}' has been used already, try again.")

  previous_guesses.append(guess)

  if (guess not in chosen_word):
    lives -= 1

    print(
      f"This letter, '{guess}' is not in the word you're trying to figure out. Try Again."
    )

    print(stages[lives])

    if (lives == 0):
      print("You Lost")
      game = False
