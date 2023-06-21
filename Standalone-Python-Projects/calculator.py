#!/usr/bin/python3

from replit import clear

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)


def add(n1, n2):
  """
  This function adds 2 numbers together.
  """
  return n1 + n2


def subtract(n1, n2):
  """
  This function subtracts 2 numbers together.
  """
  return n1 - n2


def multiply(n1, n2):
  """
  This function multiplies 2 numbers together.
  """
  return n1 * n2


def division(n1, n2):
  """
  This function divides 2 numbers together.
  """
  return n1 / n2


def exponent(n1, n2):
  """
  This function raises the 1st number to the power of the 2nd number.
  
  Example: 3 ^ 2 = 9; which raises 3 to the power of 2, which equals 9.
  """
  return n1**n2


def calculator():
  """
  This function acts as a calculator. It does a certain operation with 2 numbers, either continuing to work with the result of the 2 previous numbers or starting from scratch with 2 new numbers.
  """

  game = True

  operation_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
    "^": exponent
  }

  num1 = float(input("What's the 1st number you want? "))

  while (game):

    print("What's the operation you want to use?")

    for i in operation_dict:
      print(i)

    choice = input("Choose 1 of the operations above \n")

    num2 = float(input("What's the 2nd number you want? "))

    operation_to_run = operation_dict[choice]

    if (operation_to_run == division):
      if (num2 == 0):
        print("Value is Undefined")
        calculator()
      else:
        print(operation_to_run(num1, num2))
        num1 = operation_to_run(num1, num2)
    else:
      print(operation_to_run(num1, num2))
      num1 = operation_to_run(num1, num2)

    continue_game = input(
      f"Type 'y' to continue calculating with {num1}, or type 'n' to exit, and start a new calculation. \n"
    ).lower()

    if (continue_game == "y"):
      game = True
    else:
      game = False
      clear()
      from_scratch = input(
        "Type 'y' if you want to restart from the beginning or 'n', if you want to quit this application."
      ).lower()
      if (from_scratch == "y"):
        calculator()
      else:
        clear()


calculator()
