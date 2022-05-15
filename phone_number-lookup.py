# Python code for Phone-Number lookup
# Importing modules
from os import system
from time import sleep
import phonenumbers
from phonenumbers import timezone,geocoder,carrier

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

# inputting Values
system("clear")
inp = input(f"\n{BROWN}Enter the phone number (including courntry code){END}:{CYAN} ")

# Giving Function values
PNumber = phonenumbers.parse(f"+{inp}")
TimeZone = timezone.time_zones_for_number(PNumber)
Carrier = carrier.name_for_number(PNumber,"en")
Region = geocoder.description_for_number(PNumber,"en")

# Printing the output
print(f"\n{BLUE}{PNumber}")
print(f"{YELLOW}{TimeZone}")
print(f"{GREEN}{Carrier}")
print(f"{RED}{Region}{END}")
