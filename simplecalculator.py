# Very basic GUI based calculator
# Importing modules
from os import system
from time import sleep
import pyautogui as pg

# clearing the screen
system("clear")

# Input prompts
while True:
  a = pg.prompt("Enter the first number")
  b = pg.prompt("Enter the operation(+,-,/,*)")
  c = pg.prompt("Enter the second number")

  A = float(a)
  C = float(c)

  if b == "+":
    pg.alert(A+C)
  elif b == "-":
    pg.alert(A-C)
  elif b == "*":
    pg.alert(A*C)
  elif b == "/":
    pg.alert(A/C)
  else :
    pg.alert("ERROR! Wrong operant, Try again")

  con = pg.confirm("Do you want to exit",buttons=["YES","NO"])
  if con == "YES":
    break
