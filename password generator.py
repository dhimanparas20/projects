import random
import os

class color:
  VIOLET = '\033[95m'
  BLUE = '\033[94m'
  CYAN = '\033[96m'
  GREEN = '\033[92m'
  BROWN = '\033[93m'
  YELLOW = '\033[33m'
  BLUE = '\033[34m'
  RED = '\033[91m'
  END = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  HIGHLIGHT = '\x1b[6;30;41m'

os.system("clear")  
print("================================================")
print(f"{color.GREEN}           {color.HIGHLIGHT}{color.BOLD}{color.UNDERLINE}Welcome to MST Bash {color.END}                 ")
print("================================================")
inp = int(input(f"{color.VIOLET}Enter the length of the pasword{color.END}:{color.BLUE} "))

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = ",./;\[]<>?:|{}!@#$%^&*()_+-="

all = lower + upper + number +symbol

password= "".join(random.sample(all, inp))
print(f"{color.RED}\nGenerated password = {color.HIGHLIGHT}{color.GREEN}{password}{color.END}")

a = input(f"{color.GREEN}Do you want to save the generated password? (yes or no){color.RED}: ")
if a == "yes" or a == "YES":
  x = open("password.py", "w")
  x.write(f"Password: {password}")
  x.close()
else :
  exit()    
