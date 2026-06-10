# Without constructors
class Student:
    pass 

Student1 = Student ()
Student2 = Student()

Student1.name = "Peter"
Student1.age  = 26
Student1.marks = 395
Student1.email = "peter@gmail.com"
Student1.dob = 11-11-2005

Student2.name = "Bridgit"
Student2.age  = 28
Student2.marks = 350
Student2.email = "bridgit@gmail.com"
Student2.dob = 11-11-2001

print ("The students name is:", Student1.name, "and he is" , Student1.age, "years old." )
print ("The students name is:", Student2.name, "and he is" , Student2.age, "years old." )

# with constructors 
class Student:
    def __init__ (self,name,age,marks,email,dob):

        self.name = name 
        self.age = age
        self.marks = marks
        self.email = email
        self.dob = dob


Student1 = Student ("Peter", 20, 395, "peter@gmail.com", 11-11-2004)
Student2 = Student("Bridgit", 28, 350, "bridgit@gmail.com", 11-12-2003)

# Student1.name = "Peter"
# Student1.age  = 26
# Student1.marks = 395
# Student1.email = "peter@gmail.com"
# Student1.dob = 11-11-2005

# Student2.name = "Bridgit"
# Student2.age  = 28
# Student2.marks = 350
# Student2.email = "bridgit@gmail.com"
# Student2.dob = 11-11-2001

print ("The students name is:", Student1.name, "and he is" , Student1.age, "years old." )
print ("The students name is:", Student2.name, "and he is" , Student2.age, "years old." )

class laptop():
    def __init__(self,model,color,price):
        self.model = model
        self.color = color
        self.price = price

laptop1 = laptop("dell", "black", 95000)
laptop2 = laptop ("lenovo", "grey", 88000)

print("The cost of",laptop1.model, "is", laptop1.price, ".")
print("The cost of",laptop2.model, "is", laptop2.price, ".")

class Book():
    def __init__(self,title,author,yop):
        self.title = title
        self.author = author
        self.yop= yop

Book1 = Book ("Conspiracy?", "Peter", 1889)
Book2 = Book ("Relativity", "Albert", 1954)

print("The book",Book1.title, "written by", Book1.author, "was published in", Book1.yop,".")
print("The book",Book2.title, "written by", Book2.author, "was published in", Book2.yop,".")

