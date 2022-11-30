# Here I will be learning some concepts os Object Oriented Programming using Python
# I alredy know About Object Oriented Programming in Cpp.
from os import system
system("clear")

class Item:  #Defining name of class
  discount = 10/100
  def __init__(self, name: str, price: float, qty=0):  #Parameterized constructor with pre defined default arguments and their type
    self.name = name   
    self.price = price
    self.qty = qty
    
  def total_price(self):  #Member function
    self.total_price = self.price * self.qty
    return self.total_price
  
  def apply_discount(self):
    pass
    dicount_amt = (self.price * self.qty)*Item.discount
    return ((self.price * self.qty)- dicount_amt)
    
i1 = Item("Pen",15,10)
i2 = Item("Rubber",7)  #Here the qty of rubber will be 0 by default 
i3 = Item("Pencil",5,50)

print(i1.name)
print(i2.qty)
i2.qty = 25  #Updating the values
print(i2.qty)
print(i3.price)
print("-----------------------------")
print(i1.total_price())
print(i2.total_price())
print(i3.total_price())
print("-----------------------------")
print(i1.apply_discount())
print(i2.apply_discount())
print(i3.apply_discount())
print("-------------------------------------------------------------------")

#Understaing inheritance
class Pet():  #Base class  
  def __init__(self,name,age):
    self.name=name
    self.age=age
    
  def show(self):
    print(f"I'm {self.name} and im {self.age} yearls old.")  
  
  def speak(self):
    print("Sorry i cant speak.")  
    
class Cat(Pet): #Derived class, inheriting Pet class
  def speak(self):
    print("Meow")    

class Dog(Pet):  #Derived class, inheriting Pet class
  def speak(self):
    print("Bark")   
    
p1 = Pet("Tim",14)
p1.show()
p1.speak()

c = Cat("Tom",6)
d = Dog("Buffy",15)
c.show()
c.speak()
d.show()
d.speak()
