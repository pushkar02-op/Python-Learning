# strg = "jhvcjhbh"
# print(strg[:1])  # First char
# print(strg[-1:])  # Last char
# print(strg[1:])  # Except First
# print(strg[:-1])  # Except Last
# print(strg[1:-2])  # Betwwen two positions


# Join
# mylist = ["A", "B", "C", "D"]
# mystr = "dc BD GDGW"
# print(mystr, mylist)
# print(mystr + ",".join(mylist))

# strnew = "Welcome"
# strnew = strnew + ",".join([str(myst) for myst in mylist])
# print(strnew)


# Compare strings

# str1 = "India"
# str2 = "India"
# print(str1 is str2)
# print(str1 == str2)


# # Delete a string
# str1 = "dvhcgc"
# print(str1)
# del str1

# # String to Float
# float_str = "278712.268"
# print(type(float_str))
# str_to_float = float(float_str)
# print(str_to_float)

# # String to int
# int_str = "254"
# print(type(int_str))
# str_to_int = int(int_str)
# print(str_to_int)

# # String to bool
# bool_str = "True"
# print(type(bool_str))
# str_to_bool = bool(bool_str)
# print(str_to_bool)

# # For loop in string
# mystr = "pythonScript"
# for letter in mystr:
#     if letter != "S":
#         print("Current letter :", letter)
#     elif letter == "S":
#         break

# # Loop in a list
# items = ["Oracle", "python", "c#", "SqlServer"]
# for list_str in items:
#     if list_str != "SqlServer":
#         print("Current String", list_str)
#     elif list_str == "SqlServer":
#         break


# words = ["it", "bye", "hbe", "dw", "ejbce"]
# for idx, word in enumerate(words):
#     print(idx, word)


# # Nested list
# nest = [
#     [2, 56, [-1, -6, 9, 56, 78]],
#     5,
#     [0, 23, 7, -45, 9, 88],
#     [12, ["hello"]],
#     [12, 34, "Pratyush", "Uma", "Tuhin"],
# ]
# print(nest[4][2][::-1])


# # Dynamic list using list comprehension..
# number_list = [x for x in range(1, 400) if x % 2 == 0 if x % 5 == 0]
# print(number_list)
# print([x for x in range(1, 400) if x % 5 == 0])


# # Dictionary
# my_disc = {}
# my_disc = {1: "Orange", 2: "Ball", 3: "Bat"}
# print(my_disc)
# print(my_disc[1] + ", " + my_disc[2])

# for item in my_disc.items():
#     print(item)

# Enter values in disctionary
# d = {}
# d["dhb"] = 24
# d["jcb"] = 256
# print(d)

# # Type of disc
# d1 = {"Georg": 24, "Tom": 32, "Kasbd": 78}
# print(d1)
# print(type(d1))


# mydict = {
#     "Name": ["fejef", "einei", "dniw", "dinid"],
#     "ID": [1223, 1233, 123, 3422],
#     "Adress": ["dckdc", "knfei", "okdeod", "enfei"],
# }
# print(mydict)


# # Dictionry inside a disctionare
# fruit = {"banana": {"white": "green"}, "mango": "peach"}
# print(fruit["banana"]["white"])

# people = {
#     1: {"name": "cnwddw", "Age": 22, "Salary": "knx"},
#     2: {"name": "c23555", "Age": 29, "Salary": "34332"},
# }
# print(people)
# people[3] = {}
# people[3]["name"] = "cn ej"
# people[3]["Age"] = 56
# people[3]["Salary"] = "59040"
# print(people)
# print(len(people))
# print(type(people))
# people[1] = {"name": "dcdf", "Age": 45, "Salary": "3938"}
# print(people)
# for p_id, p_info in people.items():
#     print("PersonID", p_id)
#     for key in p_info:
#         print(key + ":", p_info[key])


# # ADDIng new keys using update()
# disc = {}
# disc = {"a": "aa", "b": "bb", "c": "cc"}
# print(disc)
# disc["d"] = "do"
# disc["e"] = "ee"
# disc["f"] = "ff"
# disc.update({"g": "Ganga"})
# disc_new = {"djb": "sbjc", "schb": "jbx", "jxb": "djb"}
# disc.update(disc_new)
# print(disc)
# del disc["djb"]
# print(disc)

# for item in disc.items():
#     print(item)


# # TUPLE
# my_data = ("hi", "hello", 2.5, -93, [1, 5, 90], (2, 4, "heks"))
# print(my_data)

# # Tuple operations
# tup = ("p", "d", "f", "r", "t", "g", "y", "c")
# print(tup[0])
# print(tup[6])

# n_tup = ("hsc sh0", [4, 4, 2], (2, 4, 5, 6))
# print(n_tup[0][2])
# print(n_tup[-1])
# print(n_tup[1][2])
# print(n_tup[0][2:])
# print(n_tup[0][0:4])

# print(("Name",) * 5)

# del tup


# Functions


# def welcome():
#     print("Welcome")


# welcome()


# def operation():
#     x = 34
#     y = 23
#     print(x + y)


# operation()


# def add(x, y):
#     return x + y


# result = add(10, 10)
# print(result)


# def expo(x):
#     return x ** 2


# print(expo(2))


# def greet(name, text):
#     print("Hello", name + "," + text)


# greet("jgvy", "dhbhjc")


# def myfxn(name, text="welcome"):
#     print("hello", name + "," + text)


# myfxn("Jane")
# myfxn("dhcdh", "chhjc ahdb")


# def Greet(*names):
#     for name in names:
#         print("Hello", name)


# Greet("chjsbh", "hbcjgh", "jdbchc", "jbch")


# def great(name, age):
#     print("Hello my name and age is " + name + " " + str(age) + ", good evening!!")
#     print("\n Thank you")


# great("Iron Man", 56)
# great("Hulk", 70)


# def function_sq(x):
#     return x * x


# def iseven(x):
#     return x % 2 == 0


# def isdiv5(x):
#     return x % 5 == 0


# list_even = [function_sq(x) for x in range(50) if iseven(x) if isdiv5(x)]
# print(list_even)


# Recursive factorial function


# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x - 1)


# given_value = int(input("Give number :- "))
# print("The factorial of ", given_value, "is ", fact(given_value))


# # Global keyword
# x = "Global"


# def myfxn():
#     print("x is inside ", x)


# myfxn()
# print("x is outside ", x)


# def func_new():
#     global x
#     x = x * 2
#     print(x)


# func_new()


# def fouter():
#     x = "Welcome"

#     def finner():
#         nonlocal x
#         x = "Awesome "
#         print("My inner fxn", x)

#     finner()
#     print("fouter", x)


# fouter()


# One fxn can retrurn two fxns
# def f(x):
#     return g(x + 1), h(x + 2)


# def g(y):
#     return y * 10, y + 10


# def h(z):
#     return z * 10, z + 10


# print(f(100))


# ###OOPS in Python
# def welcome():
#     print("Welcome")


# welcome()


# class Employee:
#     "this is Employee class"
#     Id = ""
#     Name = ""
#     Salary = ""
#     PAN = ""

#     def welcome(self):
#         print("Welcome from Employee ..")

#     def Info(self):
#         print("Welcome", self.Id)
#         print("My name is ", self.Name)
#         print("Salary is ", self.Salary)
#         print("Pan Information ", self.PAN)


# empobj = Employee()
# empobj.welcome()
# print(Employee.__doc__)
# empobj.Id = 1001
# empobj.Name = "DHV WJDVH"
# empobj.Salary = 2781782
# empobj.PAN = "KWHDYWB@%@&"
# empobj.Info()


# # Constructor
# class Student:
#     def __init__(self, name):
#         # classmember_var = instance var
#         print("Inside Constructor")
#         self.name = name

#     def show(self):
#         print("Hello , ", self.name)


# obj = Student("jhvcc")
# obj.show()
