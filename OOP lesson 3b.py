# overiding

class Animal:
    def __init__ (self,name):
        self.name = name
    def speak(self):
        print (self.name,"can bark")

class Dog(Animal):            
    def speak (self):
        print ("woof!")

d1 = Dog ('Rex')
d1.speak()        

print ('...............................')

class Shape: 
    def __init__(self, area):
        self.area = area
    def area (self):    
        print ("Area of shape is ", self.area)
class Circle (Shape):
    def __init__(self, r,num2):
        self.r = r
        self.num2 = num2
    def area (self):
        area = self.r*self.r*self.num2 
        print ("The area of circle is", area)

class Rectangle (Shape):
    def __init__(self, l,w):
        self.l = l
        self.w = w
    def area(self):    
        area = self.l*self.w
        print("The area of rectangle is", area)
            


# v1 = Shape('area')
v2= Circle(5,3.14)
v3 = Rectangle (6,7)

v2.area()
v3.area()

# Super function
# We use super to reuse the code in the parent class

class Animal :
    def __init__(self,name):
        self.name=name
class Dog(Animal):
    def __init__(self, name,age):
        # calls the parents constructors.
        super().__init__(name)
        self.age = age
d1 = Dog ("Scooby Doo", 20)
print (d1.name,"is", d1.age, "years old.") 

print ("...........................")

class Animal:
    def __init__(self, name): 
        self.name = name 
    def speak (self):
        print (self.name, "can bark.")
class Dog (Animal):
    def speak (self):
        super().speak ()
        print (self.name, "can woof.")
d1= Dog ("Rex")
d1.speak()                     