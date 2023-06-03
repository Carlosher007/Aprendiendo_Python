"""
You works in a company where the sellers receive a 13% by their total sales and your boss wants you help the sellers to calc their commisions with a program to ask the name and how much he/she has been coming
"""

from manageOptions import manageOptions  

def main():
  def askNameUser():
    return input("Enter your seller name: ")

  def askTotalSales():
    return float(input("Enter the value of your total sales: "))

  def calculateComissions(totalSales):
    return round(totalSales * (13/100),2)

  def showComissiones(name,totalSales,comissions):
    return f"{name} your total sales are {totalSales}, so you has {comissions} in commission. Thanks"

  def doAllSteps():
      name = askNameUser()
      totalSales = askTotalSales()
      comissions = calculateComissions(totalSales)
      print(showComissiones(name, totalSales, comissions))

  manageOptions(doAllSteps)

if __name__ == "__main__":
  main()
