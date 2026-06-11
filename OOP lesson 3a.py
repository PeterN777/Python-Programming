# create a child class that inhersits from its parent

class Animal:
    def __init__ (self,name):
       
       self.name =name
    def bark(self):
        print (self.name)   

# create the dog class (inherits from animal)         
class Dog (Animal):
    pass
# craete an object 
d1= Dog ("Scooby doo")

# call
d1.bark()