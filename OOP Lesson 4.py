# Enacpsulation _ Hides data when you want to 
# Create a class account with a private balance
# Private attribute --balance (initial 0)
# deposit (amount)- positive amounts
# withdraw (amount) cannot excdeed balance
# get balance returns current balance.
# Demonstrate depsoit 500, withdraw 200, attempt withdrw (1000). show  
# Final bal


# class Student:
#     def __init__ (self,name):
#         # double underscore makes variable private
#         self.__name =name
#     def display (self):
#         print (self.__name)
# s1=Student("John")
# s1.display 

# class Account:
#     def __init__ (self,initbalance):
#         self.__balance =initbalance
#     def balance (self): 
#         initialbalance = self.__balance
#         initialbalance = 0
#         print (self.__balance)
    
#     def __init__ (self, amount1):
#         self.amount1 = amount1 
     
#     def deposit (self):
#         depositamount = self.amount1
#         if self.amount1 >=0: 
#             print ("The deposit is successful")
#         else:
#             print ("Not successful")    

#     def __init__(self, amount2):
#         self.amount2 = amount2

#     def withdraw (self):
#         withdrawalamount = self.amount2
#         if self.amount2 >= self.__balance + self.amount1:
#             print  (" Withdrawal of", self.amount2, " is not successfel.")
#         else: 
#             print ("Withrawal of", self.amount2, "is successful.")
    
#     def finalbalance (self): 
#         finalbalance = self.__balance + self.amount1 - self.amount2
#         print ("Your balance is", self.__finalbalance)


# A1 = Account (500)
# A2 = Account (200)

# A1.account()
# A2.account()

class Account:
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        print (self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit 0f",amount, "is successful.")
        else:
            print("Deposit failed.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal of", amount, "is successful.")
        else:
            print("Withdrawal of", amount, "failed.", "Insufficient funds.")

my_account = Account()
print("Starting Balance", my_account.get_balance())
my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(1000)
print ("Final Balance", my_account.get_balance())

class Animal:
    def __init__(self, name):
        self.name= name
    def speak(self):
        print (self.name,"crys.")
class Dog(Animal):
    def speak(self):
        print (self.name,"Woofs")
Lion= Animal("Scoob")
Lion.speak ()        
sound2= Dog("Scooby")
sound2.speak()

def find_sum(n): 
    for num in range (1,n+1):
        sum = ((n*(n+1))//2)

print ("Find_sum",(5)) 

def find_sum(n):
    return (n * (n + 1)) // 2
print(find_sum(20))

def find_sum(n):
    total = 0
    for num in range(1, n + 1):
        total += num
    return total
print (find_sum (6))



def count_vowels(word):
    count = 0
    word = word.lower()
    for letter in word:
        if letter in "aeiou":
                count += 1
    return count

print(count_vowels("Arsenal"))

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def display (self):
        print (self.name,self.grade)
Student1 = Student("Peter,", "A.") 
Student1.display() 

class Car:
    def __init__ (self):
        self.__speed = 0
    def get_speed(self):
        print (self.__speed)

    def accelerate(self):
        self.__speed += 10

    def brake(self):
        if self.__speed >=5:
            self.__speed -=5
        else:
            self.__speed = 0.
    def showspeed(self):
        print ("The current speed is", self.__speed)

car1= Car()
car1.accelerate()
car1.accelerate()
car1.accelerate()
car1.brake()
car1.showspeed()   

class Person:
    def __init__ (self,name,age):
        self.name = name
        self.age= age
class Student (Person):
     def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
     def display(self):
        print(self.name)
        print(self.age)
        print(self.course)

student1 = Student("Peter", 26, "Chemical Engineering")
student1.display()




