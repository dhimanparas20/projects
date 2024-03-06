from os import system
from time import sleep


system("clear")
print("--------------------------------------------")
inp = int(input("1: To configure mega account.\n2: To upload file to mega.\n3: Exit.\n\n--> "))

if inp == 1:
  system("sudo apt update && sudo apt install rclone && rclone config ")
  system("python3 rclone.py")

elif inp == 2:
  fname = input("Enter name of file: ")
  #rname = input("Enter name of Mega Remote: ")
  rname = "meag"
  folder = input("Enter the folder name  to save file into (default root /): ")
  if folder == None:
    folder = "" 
  system(f"rclone -P copy {fname} {rname}:{folder}")

elif inp == 3:
  exit()
