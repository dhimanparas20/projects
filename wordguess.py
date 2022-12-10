from os import system
from time import time,sleep
system("clear")

lst = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] # Stored list of alphabets
print("\n\n-----------------------------------------------------")
print("Think of a word in your mind of length 3-6 words.")
print("-----------------------------------------------------")
len =  int(input("Enter the length of the word (3-6): ")) # Takes user input of length of the word.

if len < 3 or len >6 : # Checks if the length of word exceeds or preceeds the desired limit
  system("clear")
  print("The length is out of the range/limit.\nPLease try again.")
  sleep(1)
  system("python3 wordguess.py")

print()
for i in range(1,len+1): # Prints the column Number.
  print(i,end=" | ")
print()

for i in range(26): # Prints the alphabets in the desired matrix
  print(lst[i],end=" | ")
  if i == len-1 or i == 2*len-1 or i == 3*len-1 or i == 4*len-1 or i == 5*len-1 or i == 6*len-1  or i == 7*len-1 or i == 8*len-1:
    print(" ") 
print("\n")

inp = [None] * 6 #created empty(None) list of size 6
for i in range(0,len): #Stores the number of column having N alphabets in list inp
  inp[i] = int(input(f"Enter the column having Alphabet {i+1}: "))


system("clear")
print()
for i in range(1,10): # Prints the column Number.
  print(i,end=" | ")
print()

# Created 6 empty lists to store all the alphabets of a column in each list
tmp1 = [None] * 30
tmp2 = [None] * 30
tmp3 = [None] * 30
tmp4 = [None] * 30
tmp5 = [None] * 30
tmp6 = [None] * 30

for i in range(0,len): # Stores the alphabets of a column in each list
  j,k = 0,0
  while j < 26:
    print(lst[(inp[i]-1)+j], end = " | ") # Prints the alphabets of selected column in the new matrix
    if i == 0:    # Stores the alphabets of column1 in  list tmp1
      tmp1[k] = lst[(inp[i]-1)+j]
    elif i == 1:  # Stores the alphabets of column2 in  list tmp2
      tmp2[k] = lst[(inp[i]-1)+j]
    elif i == 2:  # Stores the alphabets of column3 in  list tmp3
      tmp3[k] = lst[(inp[i]-1)+j]
    elif i == 3:  # Stores the alphabets of column4 in  list tmp4
      tmp4[k] = lst[(inp[i]-1)+j]
    elif i == 4:  # Stores the alphabets of column5 in  list tmp5
      tmp5[k] = lst[(inp[i]-1)+j]        
    elif i == 5:  # Stores the alphabets of column6 in  list tmp6
      tmp6[k] = lst[(inp[i]-1)+j] 
    j +=len  # created gap between the next element of the matrix
    k +=1
    if (inp[i]-1)+j >= 26:
      break
  print()

print()
inp2= [None] * 6
for i in range(0,len):  #Stores the number of column having N alphabets in list inp2
  inp2[i] = int(input(f"Enter the column having Alphabet {i+1}: "))
print()

word = [None] * 6  # This list will store all the  final alphabets
num = 0
def ret(tmpp,i,num):  # Stores all the  final alphabets to the list word
  if tmpp[i] != None:
    word[num]= tmpp[inp2[i]-1]
    #print (tmpp[inp2[i]-1],end= "")

str = [tmp1,tmp2,tmp3,tmp4,tmp5,tmp6]
for i in range(0,len): # Sends names of temperary lists (tmp1...tmp6) stored in list "str[]" one by one to ret() function
  ret(str[i],i,num)
  num += 1
print()

system("clear")
print()
print("-----------------------------------------------------")
print("\t\tYour word is ")
print("-----------------------------------------------------\n")
for i in range(0,len):  # Finally prints the word by accessing the alphabets stored in list "word[]"" one by one.
  print(word[i],end="")
print("\n\n") 
