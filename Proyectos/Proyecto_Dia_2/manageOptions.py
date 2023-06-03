"""
The idea is do a while bucle where you can ask to user if he/she wants to follow or cancel the process. This function must be able to be reusable .
"""

import os

def manageOptions(steps):
  def handleOption(option, action):
    if option.lower() == "s":
      os.system('clear')
      action()
    elif option.lower() == "n":
      return False
    else:
      print("Enter a valid option")
    return True

  def bucle():
    os.system('clear')
    steps()

    while True:
      print()
      option = input("Do you want to continue? (S/N) ")
      if not handleOption(option, steps):
        break

  bucle()

