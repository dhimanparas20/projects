# Python made infinite running Bash Shell 
import os

class colors:
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
print(f"{colors.GREEN}           {colors.HIGHLIGHT}{colors.BOLD}{colors.UNDERLINE}Welcome to MST Bash {colors.END}                 ")
print("================================================")
print(f'''1: {colors.VIOLET}VIOLET{colors.END}
2: {colors.BLUE}BLUE{colors.END}
3: {colors.CYAN}CYAN{colors.END} 
4: {colors.GREEN}GREEN{colors.END}  
5: {colors.BROWN}BROWN{colors.END}
6: {colors.YELLOW}YELLOW{colors.END} 
7: {colors.BLUE}BLUE{colors.END} 
8: {colors.RED}RED{colors.END}
9: Default color
NOTE: Colors may vary terminal to terminal.''') 

print("================================================")

pcolor = ""
scolor = ""
inp1 = int(input("\nEnter the color number of preceeding shell from above: "))
if inp1 == 1:
  precolor = colors.VIOLET
elif inp1 == 2:
  precolor = colors.BLUE
elif inp1 == 3:
  precolor = colors.CYAN
elif inp1 == 4:
  precolor = colors.GREEN
elif inp1 == 5:
  precolor = colors.BROWN
elif inp1 == 6:
  precolor = colors.YELLOW
elif inp1 == 7:
  precolor = colors.YELLOW
elif inp1 == 8:
  precolor = colors.BLUE
elif inp1 == 9:
  precolor = ""
else: 
  exit()

pcolor = precolor  

inp2 = input("Do you want to BOLD out preceeding shell? (yes or no): ")
if inp2 == "yes" or inp2 =="YES":
  bold = colors.BOLD
elif inp2 == "no" or inp2 == "NO":
  bold = ""  
else:
  bold = ""

inp3 = input("DO you want to UNDERLINE preceeding shell?(yes or no): ")
if inp3 == "yes" or inp2 =="YES":
  underline = colors.UNDERLINE
elif inp3 == "no" or inp3 == "NO":
  underline = ""  
else:
  underline = ""

inp4 = input('''DO you want to HIGHLIGHT preceeding shell? 
NOTE: preceding color will be lost (yes or no):''')
if inp4 == "yes" or inp4 =="YES":
  highlight = colors.HIGHLIGHT
elif inp4 == "no" or inp4 == "NO":
  highlight = ""  
else:
  highlight = ""

inp5 = int(input("Enter the color number of suceeding shell from above: "))
if inp5 == 1:
  succolor = colors.VIOLET
elif inp5 == 2:
  succolor = colors.BLUE
elif inp5 == 3:
  succolor = colors.CYAN
elif inp5 == 4:
  succolor = colors.GREEN
elif inp5 == 5:
  succolor =colors.BROWN 
elif inp5 == 6:
  succolor = colors.YELLOW 
elif inp5 == 7:
  succolor = colors.YELLOW
elif inp5 == 8:
  succolor = colors.BLUE  
elif inp5 == 9:
  succolor = ""
else: 
  exit() 

scolor = succolor    
 
i = 0
while i <= 1:
  a = input(f"{colors.END}{pcolor}{bold}{underline}{highlight}$Command{colors.END}{scolor}: ")
  os.system(a)
  if a == "exit" :
    i = 1
    exit()
  else:
    i = 0  
exit()    
