# Class Calcualtor

class Calculator:
    def __init__ (self, num1,num2):
        self.num1 =num1
        self.num2 =num2

    def add(self): 
         print ("The sum is", self.num1+self.num2 )
    def subtract (self):   
         print ("The difference is", self.num1-self.num2 )
    def multiply (self):
         print ("The product is", self.num1*self.num2)
    def divide (self):
         print (f"The division is{self.num1/self.num2}" )
    

calc1= Calculator(5,5)           

calc1.add()
calc1.subtract ()
calc1.multiply()
calc1.divide () 


class Student:
     def __init__(self,name,grade):
          self.name = name
          self.grade = grade
s1= Student ("Anna", "A")
print (s1.grade)

s1.grade ="B"
print (s1.grade)
        