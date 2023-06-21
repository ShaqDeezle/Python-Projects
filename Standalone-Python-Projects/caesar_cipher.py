#!/usr/bin/python3

import replit
import time

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP""" """"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""" """" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

retry = True


def caesar(input_text, shift_amount, decision):
  """This function's goal is to take text and shift that text to a certain number based on the 'shift amount', based on whether you want to 'encode' or 'decode' your message."""

  new_word = []

  for i in input_text:

    if (i not in alphabet):
      new_word.append(i)

    else:

      original_index = alphabet.index(i)

      if (decision == "encode"):

        next_index = (original_index + shift_amount)

        if (next_index >= 26):
          while (next_index not in range(0, 26)):
            next_index -= 26

      elif (decision == "decode"):

        next_index = (original_index - shift_amount)

        if (next_index <= -1):
          while (next_index not in range(0, 26)):
            next_index += 26

      new_word.append(alphabet[next_index])

  cipher_text = "".join(new_word)

  print(f"The {decision}d text is: '{cipher_text}'")


while (retry):

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

  direction_options = ["encode", "decode"]

  if (direction not in direction_options):
    print("Please choose a valid option. Either 'Encode' or 'Decode'.")

  else:

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    caesar(input_text=text, shift_amount=shift, decision=direction)

  print("\n")

  choice = input(
    "Would you like to restart the Cipher Program? Type 'Yes' or 'No'. \n"
  ).lower()

  if (choice == "yes"):
    retry = True
  else:
    print("Goodbye.")
    retry = False
    time.sleep(7)
    replit.clear()
