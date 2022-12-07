# Trying to make a dynamic clock.
# For now only clock and alarm works.
from time import sleep,time
from os import system
from playsound import playsound

system("clear")
class Clock:
  def __init__(self,hh,mm,ss=00):
    self.hh = hh
    self.mm = mm
    self.ss = ss
    
  def set_alarm(self,HH,MM,SS=0): #Playing the alarm
    if self.hh == HH and self.mm == MM and self.ss == 0:
      seconds = 10
      end_time = time() + seconds      
      while time() < end_time:
        playsound("beep.mp3")
      self.ss += 11
  
  def run(self,HH,MM,SS=0): #Mian clock code
    while True:
      sleep(1)   #The thing that delays per sec.
      system("clear") #this clears system after every second.
      self.ss += 1
      if self.ss==60:
        self.ss = 0
        self.mm +=1
        if self.mm == 60:
          self.mm = 0
          self.hh += 1
          if self.hh == 24:
            self.hh= 0
            
      print("-------------------")      
      print(f"|Time:   {self.hh}:{self.mm}:{self.ss} |")
      print("-------------------")
      print("\n-----------------")      
      print(f"|Alarm:   {HH}:{MM} |")
      print("-----------------")
      self.set_alarm(HH,MM)    
   
print("---------------------------------------------")
h = int(input("Enter Current Hour: "))
m = int(input("Enter Current Minutes: "))
print("---------------------------------------------")
hh = int(input("Enter Alarm Hour: "))
mm = int(input("Enter Alarm Minute: "))
if h>24 or hh > 24 or m>60 or mm>60:
  system("clear")
  print("Invalid input. Please try again")
  sleep(2)
  system("python3 clock.py")

c1 = Clock(h,m)
c1.run(hh,mm)


