# Inporting modules
import pyqrcode
import png
from pyqrcode import QRCode
from os import system
import os.path
from os import path
from time import sleep

# Defining colors
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
HIGH = '\x1b[6;30;42m'
HIGHLIGHT = '\x1b[6;30;43m'

# Inputng values
system("clear")
inp = input(f"{CYAN}Enter the URL/Text to generate QR code:{YELLOW} ")
inp2 = input(f"{CYAN}Enter the name of the file generated:{YELLOW} ")
inp3 = int(input(f"{CYAN}Enter the Scale of QR code (type 0 for default-8):{YELLOW}"))
print("")

# conditionising the scale size
if inp3 == 0 :
  size = 8

elif inp3 >=50 :
  print(f"\n{RED}{HIGHLIGHT}Size limit exceeded{END}")
  sleep(2)
  system("python3 QRgen.py")

else:
  size = inp3

# making the output folder
if (path.exists('QR_output') == True) :
  print(f"{END}output folder alredy exists")

else:
  system("mkdir QR_output")

# Generating the QR code
url = pyqrcode.create(inp)
# Saving the QR to output folder
url.png(f"QR_output/{inp2}.png",scale = size)
print(f"\n{BLUE}QR code generated sucessfully{END}")
sleep(1)
# Opening the generated QR code
system(f"feh QR_output/{inp2}.png")
