from os import system
from time import time,sleep

def clear():
  system("clear")

clear()
lst = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",
"Z","0","1","2","3","4","5","6","7","8","9",".",",","!","@","#","%","*","(",")","?","/","-","+",":",";","'","\"",
"|","<",">"] #Storing of all the characters in a list

inp = input("Enter your String: ")  # Takes string input from the USER
tmp = [None] * 500
str = inp.upper() # Converts the alphabets into Upper Case
len = len(str) # Finds out the length of the USER entered String

for word  in str:  # IF  the user entered character is not in the List it will re run the program.
  if word not in lst:
    print(f"character: {word} not in the list.")
    sleep(1)
    system("python3 text_print.py")

# Main code begins here-after
n = 0
for word in str: # This parses each charcter of the string.
  for i in range(57): # Loop to goto each element of the list
    print("----------------------------------")
    if tmp[n-1] != None:
      for j in range (len):
        if tmp[j] != None:
          print(tmp[j],end= "") # Prints the previously stored chasracters.
      print(lst[i])  
    else:
      print(lst[i]) # prints each character of list one by one
    sleep(0.050)    # delays the code
    clear()         # clears the screen for the needed effect
    if lst[i] == word:
      tmp[n] = word # If the user entered character matches the list character it will store it in a temperary list.
      break    # Break the loop
  n +=1

print("----------------------------------")  
for i in range (len): #Prints the full String
  print(tmp[i],end="") 
print("\n----------------------------------")