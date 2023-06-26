import menu
from art import logo

continue_dispense_coffee = True

number_of_drinks_bought = 0

drinks_you_want = []

insert_change = {
  "Quarters": ".25",
  "Quarter": ".25",
  "Dimes": ".10",
  "Dime": ".10",
  "Nickels": ".05",
  "Nickel": ".05",
  "Pennies": ".01",
  "Penny": ".01" 
}

change = []

print(logo)

while (continue_dispense_coffee):

  coffee_choice = input("\nWhat would you like? Coffee, a 'Report' of available resources, or turn 'Off' the machine?: ").lower()

  if (coffee_choice == "off"):
    continue_dispense_coffee = False

  
  elif (coffee_choice == "report"): 
    
    if (number_of_drinks_bought == 0) and (not drinks_you_want):
      
      menu.resources["money"] = 0
      
      for keys, values in menu.resources.items():
        
        if (keys.lower() == "coffee"):
          print(f"{keys.title()} left: {values}g")
        
        elif (keys.lower() == "money"):
          print(f"{keys.title()} spent: ${values}")
        
        else:
          print(f"{keys.title()} left: {values}ml")
  
    elif (number_of_drinks_bought > 0) and (drinks_you_want):
      
      water = 0
      milk = 0
      coffee = 0
      cost = 0
      
      for i in drinks_you_want:
        
        water += menu.MENU[i]["ingredients"]["water"]
        
        if ("milk" in menu.MENU[i]["ingredients"]):
          milk += menu.MENU[i]["ingredients"]["milk"]
        
        else:
          milk += milk

        coffee += menu.MENU[i]["ingredients"]["coffee"]

        cost += menu.MENU[i]["cost"]
        
  
      menu.resources["money"] = cost
      
      for keys in menu.resources.keys():
        
        if (keys.lower() == "coffee"):   
          remaining_coffee = (menu.resources["coffee"] - coffee)
          
          if (remaining_coffee >= 0):
            print(f"{keys.title()} left: {remaining_coffee}g")

        elif (keys.lower() == "money"):
          money_spent = menu.resources["money"]
          
          if (len(str(money_spent)) == 3):
            print(f"{keys.title()} spent: ${money_spent}0.")
          
          else:
            print(f"{keys.title()} spent: ${money_spent}.")
          
        elif (keys.lower() == "milk"):
          remaining_milk = (menu.resources["milk"] - milk)
  
          if (remaining_milk >= 0):
            print(f"{keys.title()} left: {remaining_milk}ml")
  
        elif (keys.lower() == "water"):
          remaining_water = (menu.resources["water"] - water)
  
          if (remaining_water >= 0):
            print(f"{keys.title()} left: {remaining_water}ml")
  

  elif (coffee_choice == "coffee"):
    
    type_of_coffee = input("What type of coffee do you want? 'Espresso', 'Latte', or 'Cappuccino'? \n").lower()

    if (type_of_coffee != "espresso") and (type_of_coffee != "latte") and (type_of_coffee != "cappuccino"):
      
      print("You chose an incorrect option. Please try again from the beginning.")
      
      continue_dispense_coffee = False

    elif (type_of_coffee == "espresso") or (type_of_coffee == "latte") or (type_of_coffee == "cappuccino"):
    	
      if (type_of_coffee == "espresso"):	
        number_of_drinks_bought += 1	
        drinks_you_want.append(type_of_coffee)	
        	
      elif (type_of_coffee == "latte"):	
        number_of_drinks_bought += 1	
        drinks_you_want.append(type_of_coffee)
        
      elif (type_of_coffee == "cappuccino"):	
        number_of_drinks_bought += 1	
        drinks_you_want.append(type_of_coffee)
  
      water = 0
      milk = 0
      coffee = 0
      
      for i in drinks_you_want:
        
        water += menu.MENU[i]["ingredients"]["water"]
        
        if ("milk" in menu.MENU[i]["ingredients"]):
          milk += menu.MENU[i]["ingredients"]["milk"]
        
        else:
          milk += milk
  
        coffee += menu.MENU[i]["ingredients"]["coffee"]
  
      
      for keys in menu.resources.keys():
        
        if (keys == "coffee"):   
          remaining_coffee = (menu.resources["coffee"] - coffee)
          
          if (remaining_coffee < 0):
            print("\nThere's not enough coffee to make this drink.")
          
        elif (keys == "milk"):
          remaining_milk = (menu.resources["milk"] - milk)
  
          if (remaining_milk < 0):
            print("\nThere's not enough milk to make this drink.")
  
        elif (keys == "water"):
          remaining_water = (menu.resources["water"] - water)
  
          if (remaining_water < 0):
            print("\nThere's not enough water to make this drink.")
      
      if (remaining_coffee < 0) or (remaining_milk < 0) or (remaining_water < 0):

        drinks_you_want.pop()
      
        total_drinks_bought = ", ".join(drinks_you_want)
  
        print(f"\nThank You for purchasing your {total_drinks_bought.title()} with us today. Have a Great Day, and enjoy your coffee!")
  
        continue_dispense_coffee = False
  
      elif (remaining_coffee >= 0) or (remaining_milk >= 0) or (remaining_water >= 0):
        
        total = input("\nPlease insert your change for coffee. \nType the amount of each you want to insert. \nEx: 1 quarter, 2 dimes, 1 nickel, 2 pennies, etc. \n").lower()
        
        for keys, values in insert_change.items():
          total = total.replace(keys.lower(), f"*{values}")
        
        total = total.replace(" ", "")
        
        total = total.replace(",", "+")
  
        new_total = eval(total)
  
        rounded_new_total = round(new_total, 2)
  
        if (len(str(rounded_new_total)) == 3):
          print(f"\nYou inserted {total} which is ${rounded_new_total}0.")
        
        else:
          print(f"\nYou inserted {total} which is ${rounded_new_total}.")
  
        if (new_total == menu.MENU[type_of_coffee]["cost"]):
          
          print("\nYou're good to go. You paid the correct amount.")
  
          new_drink = input("\nWould you like another cup of coffee? 'Y' for yes, 'N' for no.\n").upper()
  
          if (new_drink == "N"):
            continue_dispense_coffee = False
          
        elif (new_total < menu.MENU[type_of_coffee]["cost"]):
          
          difference_in_cost = (menu.MENU[type_of_coffee]["cost"] - new_total)
  
          rounded_difference = round(difference_in_cost, 2)
          
          if (len(str(rounded_difference)) == 3):
            print(f"\nSorry that's not enough money. Money refunded. You're missing ${rounded_difference}0.")
  
          else:
            
            drinks_you_want.pop()
            
            print(f"\nSorry that's not enough money. Money refunded. You're missing ${rounded_difference}.")
  
          new_drink = input("\nWould you like another cup of coffee? 'Y' for yes, 'N' for no.\n").upper()
          
          if (new_drink == "N"):
            continue_dispense_coffee = False
          
        elif (new_total > menu.MENU[type_of_coffee]["cost"]):
          
          difference_in_cost = (new_total - menu.MENU[type_of_coffee]["cost"])
          
          rounded_difference = round(difference_in_cost, 2)
          
          if (len(str(rounded_difference)) == 3):
            print(f"\nYou overpaid, here's your change: ${rounded_difference}0.")
  
          else:
            print(f"\nYou overpaid, here's your change: ${rounded_difference}.")
  
          new_drink = input("\nWould you like another cup of coffee? 'Y' for yes, 'N' for no.\n").upper()
      
          if (new_drink == "N"):
            continue_dispense_coffee = False
  
    else:
      print("You chose an incorrect option. Try again.")
