# Import Libraries
import requests, json 
from os import system 

# Making a GET request 
system("clear") #Clears the previous session screen
uname  =  input("Enter the username: ")
print("")
r = requests.get(f"https://api.github.com/users/{uname}")
x = r.json()  # converts the API call to JSON format

print(f"url link = {r.url}")  #prints url
print(f"Rsesponse code = {r.status_code}") #prints status code
print(f"Response code less than 200 = {r.ok}")  #Returns True if status_code is less than 200
print(f"user name = {x['name']}")  #Prints username
print("")
print(x) # prints the whole JSON structure
