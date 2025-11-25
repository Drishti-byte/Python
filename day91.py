#program to demonstrate multiple inheritance 
class Animal:
    def info(self):
        print("Animals with wings")
class Mammal:
    def info(self):
        print("Mammals can give birth to their ones") 
class Bat(Animal, Mammal):
    def display(self):
        Mammal.info(self)
        Animal.info(self)
b = Bat()
b.display() 