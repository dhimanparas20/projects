# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Derived class 1
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class 2
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Derived class 3
class Fish(Animal):
    def speak(self):
        return f"{self.name} can't speak, but it swims!"

# Creating objects of different classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
fish = Fish("Nemo")

# Polymorphism: Calling the speak method on different objects
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
print(fish.speak()) # Output: Nemo can't speak, but it swims!
