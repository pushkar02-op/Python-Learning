# # Sets
# myset = set(["a", "b", "c"])
# print(myset)
# mySet = {23.9, "Welcome", (12, 36, 87)}
# # print(mySet)
# # mySet.add("adhbcdh")
# # print(mySet)

# for i in range(1, 30):
#     mySet.add(i)
# print(mySet)


# # Union between two sets
# people = {"Jay", "dhc", "dcbhd"}
# vampires = {"cjbu", "jbcu"}
# dracula = {"djv", "eh"}
# popul = people.union(vampires)
# print(popul)

# popul = people | dracula
# print(popul)

# # Intersection between sets
# set1 = set()
# set2 = set()
# for i in range(5):
#     set1.add(i)
# for i in range(3, 9):
#     set2.add(i)
# set3 = set1.intersection(set2)
# print(set3)
# set3 = set1 & set2
# print(set3)


# # Difference between sets
# set1 = set()
# set2 = set()
# for i in range(5):
#     set1.add(i)
# for i in range(3, 9):
#     set2.add(i)
# set3 = set1.difference(set2)
# print(set3)
# set3 = set1 - set2
# print(set3)

# # clear set
# set1 = {
#     1,
#     3,
#     4,
#     2,
#     42,
# }
# print(set1)
# set1.clear()
# print(set1)


# # Exception handling
# try:
#     a = int(input("Enter number:"))
#     b = int(input("Enter a number "))
#     print(str(a / b))
# except (ZeroDivisionError):
#     print("Division by zero not allowed")
# except (ValueError):
#     print("Must enter integer value")
# except:
#     print("Something went wrong")

# try:
#     num1, num2 = eval(input("Enter 2 number seperated by comma"))
#     result = num1 / num2
#     print(result)
# except ZeroDivisionError:
#     print("Division by xero not allowed")
# except SyntaxError:
#     print("Comma is missing")
# except:
#     print("Wrong input")
# else:
#     print("No exception")
# finally:
#     print("This will execute no matter what")


# # Files handling
# file = open(r"C:\Users\pushk\Desktop\Python training\Test.txt", "w")
# file.write("this is a test file written from Python code")
# file.close()

# File handling append
# file = open(r"C:\Users\pushk\Desktop\Python training\Test.txt", "a")
# file.write("\nthis is written to test append method")
# file.close


# # OOps Continued


# class Robot:
#     name = ""
#     color = ""
#     weight = ""
#     modelnumber = ""
#     price = ""

#     # Constructor
#     def __init__(self, name, color, weight, modelnumber, price):
#         self.name = name
#         self.color = color
#         self.weight = weight
#         self.modelnumber = modelnumber
#         self.price = price

#     def show(self):
#         print("My Name is", self.name)
#         print("My Color is", self.color)
#         print("My Weight is", self.weight)
#         print("My Modelmnumber is", self.modelnumber)
#         print("My Price is", self.price)


# obj1 = Robot("Pushkar", "Red", "40", "IDWUYD", "$2718")
# obj1.show()

# obj2 = Robot("hulk", "green", "80", "IDWHJDBHW", "$2818")
# obj2.show()


# # Dynamic method
# from os import name


# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sing(self, song):
#         return "{} sings {}".format(self.name, song)


# obj1 = student("dib", 67)
# print(obj1.sing("dhabh"))


# ##
# class Computer:
#     def __init__(self):
#         self.__maxprice = 1000

#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))

#     def setMaxPrice(self, price):
#         self.__maxprice = price


# obj1 = Computer()
# obj1.sell()
# obj1.__maxprice = 1200 #Cannot change the class var because it is private
# obj1.sell()
# obj1.setMaxPrice(1200)
# obj1.sell()


# Inheritance

# Syntax....
# class derived-class(base class):
#     <class-suite>


# class derived-class(base class):
#     <class-suite>
# A class can inherit multiple classes by mentioning all
# of them inside the bracket.
# Consider the following syntax...
# Syntax..
# class derive-class(<base class 1>, <base class 2>, ..... <base class n>):
#     <class - suite>


# class Animal:
#     def speak(self):
#         print("Animal Speaking")

#     def bark(self):
#         print("Animal is barking")

#     def smiling(self):
#         print("Smiling is good for health")

#     def cansmell(self):
#         print("Smelling for hungry..")


# class Dog(Animal):
#     print("Dog barking")


# class Cat(Animal):
#     print("Cat is smiling..")


# d = Dog()
# c = Cat()
# d.speak()
# c.smiling()
# d.speak()
# c.bark()


# ##
# class Bird:
#     def __init__(self):
#         print("My base bird is working...")

#     def identification(self):
#         print("Bird")

#     def swim(self):
#         print("Can swim")


# class Parrot(Bird):
#     def __init__(self):
#         super().__init__()
#         print("Parrot is ready")

#     def identification(self):
#         print("Parrot")

#     def run(self):
#         print("Run Faster")


# p = Parrot()
# p.identification()
# p.run()
# p.swim()


# # Polymorphism
# class Parrot:
#     def fly(self):
#         print("Parrot can fly")

#     def swim(self):
#         print("Parrot cannot swim")


# class Swan:
#     def fly(self):
#         print("Swam can not fly")

#     def swim(self):
#         print("swam can swim")


# def common(Bird):
#     Bird.fly()
#     Bird.swim()


# p = Parrot()
# s = Swan()
# common(s)
# common(p)


# # Multi Level Inheritance
# class Animal:
#     def speak(self):
#         print("Animal speaking")
# class Dog(Animal):
#     def bark(self):
#         print("Dog barking")
# class DogChild(Dog):
#     def eat(self):
#         print("Eating bread..")
# d=DogChild()
# d.bark()
# d.speak()
# d.eat()


# ## printing using orbject in a list
# class Studen:
#     def __init__(self, name, roll, address, marks):
#         self.name = name
#         self.roll = roll
#         self.address = address
#         self.marks = marks


# list = []
# list.append(Studen("iron man", 1, "dshcd", 67))
# list.append(Studen("hulk", 2, "djgcd", 98))
# list.append(Studen("Thor", 3, "jkg", 37))
# list.append(Studen("Loki", 4, "tujsnjs", 100))

# for i in list:
#     print(i.name, i.roll, i.address, i.marks)


# # Multiple Inheritance
# class Calculation1:
#     def Summation(self, a, b):
#         return a + b


# class Calculation2:
#     def Multiplication(self, a, b):
#         return a * b


# class expo:
#     def exponent(self, x):
#         return x ** 2


# class Derived(Calculation1, Calculation2, expo):
#     def Divide(self, a, b):
#         return a / b


# d = Derived()
# print(d.Summation(100, 38))
# print(d.Multiplication(100, 38))
# print(d.Divide(100, 38))
# print(d.exponent(10))


# # Connect to mysql db
# import mysql.connector

# database = mysql.connector.connect(host="localhost", user="root", passwd="admin")

# # preparing a cursor object
# cursorobject = database.cursor()

# # creating db
# cursorobject.execute("Create Database studentdb")


# Creating a table

# # Connect to mysql db
# import mysql.connector

# database = mysql.connector.connect(
#     host="localhost", user="root", passwd="admin", database="studentdb"
# )

# # preparing a cursor object
# cursorobject = database.cursor()

# studentrecord = """Create table Student(Name Varchar(20) Not null,branch varchar(50),Roll int not null, section varchar(5), age int)"""

# # creating db
# cursorobject.execute(studentrecord)

# database.close()


# # Insert data in table

# import mysql.connector

# database = mysql.connector.connect(
#     host="localhost", user="root", passwd="admin", database="studentdb"
# )

# # preparing a cursor object
# cursorobject = database.cursor()

# sql = "INSERT INTO STUDENT (NAME, BRANCH,ROLL,SECTION,AGE) VALUES (%s, %s, %s, %s, %s)"
# val = [
#     ("Akash", "MM", "34", "A", "5"),
#     ("Neel", "MM", "34", "B", "5"),
#     ("Rohan", "MM", "4", "C", "5"),
#     ("Amit", "MM", "3", "A", "5"),
#     ("Anil", "MM", "2", "G", "6"),
#     ("Megha", "MM", "1", "H", "5"),
#     ("Sita", "MM", "6", "A", "6"),
# ]


# cursorobject.executemany(sql, val)
# database.commit()


# print(cursorobject.rowcount, "details inserted")


# # disconnecting from server
# database.close()
