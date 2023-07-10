"""
The idea is do a while bucle where you can ask to user if he/she wants to follow or cancel the process. This function must be able to be reusable .
"""

def manageOptions(steps):

  def handleOption(option, action):
    if option.lower() == "s":
      action()
    elif option.lower() == "n":
      return False
    else:
      print("Enter a valid option")
    return True

  def bucle():
    steps()

    while True:
      option = input("Do you want to continue? (S/N) ")
      if not handleOption(option, steps):
        break

  bucle()

