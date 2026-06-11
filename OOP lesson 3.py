# OOP Methods

class Student:
    def __init__ (self,name,age,email):

        self.name =name
        self.age = age
        self.mail = email

# defining methods
    def eat (self):
        print(Student1.name, "can eat peaches")
    def sleep(self): 
        print (Student1.name, "is going to sleep.")   


Student1 = Student("Peter", 25, 'peter@gmail.com')

Student1.eat()
Student1.sleep()



class Car:
    def __init__ (self,model,yom,color):
        self.model = model
        self.yom = yom
        self.color = color
    def purchase(self):   
        print (c1.model,"will be purchased")
       
c1= Car ("Mitsubishi", 2023, "will be purchased")
c1.purchase()