# DEl Keyword:

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Laiba")

# del s1
print(s1.name)

# PRIVATE KEYWORD __

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_password(self):
        print(self.__acc_pass)

a1 = Account(1234, "abcde")

print(a1.acc_no)
# print(a1.__acc_pass)
print(a1.reset_password())

class Person:
    __name = "Anonymous"

    def __hello(self):
        print("Hello Person")

    def welcome(self):
        self.__hello()

p1 = Person()
# print(p1.__name)
# print(p1.__hello)
print(p1.welcome())

# INHERITANCE:
 
# class Car:
#     # color = "black"
#     @staticmethod
#     def start():
#         print("Car Started....")
    
#     @staticmethod
#     def stop():
#         print("Car Stopped....")

# class Toyota(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = Toyota("Fortuner")
# car2 = Toyota("Prius")

# print(car1.name)
# print(car1.start())
# print(car1.color)

# TYPES OF INHERTANCE:

# MULTI LEVEL INHERTANCE

class Car:
    @staticmethod
    def start():
        print("Car Started....")
    
    @staticmethod
    def stop():
        print("Car Stopped....")

class Toyota(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(Toyota):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("Diesel")
print(car1.start())

# MULTI LEVEL INHERITANCE

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

# SUPER KEYWORD

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started....")
    
    @staticmethod
    def stop():
        print("Car Stopped....")

class Toyota(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start

c1 = Toyota("Prius", "Electric")
print(c1.type)

# Class Method:

class Person:
    name = "Anonymous"

    def changeName(self, name):
        # Person.name = name  #first way to changen class attribute
        self.__class__.name = name #second way to change class attribute

p1 = Person()
p1.changeName("Laiba Khan Yousufzai")
print(p1.name)
print(Person.name)

# CLASS METHOD
"""
Instead of doing it like this....

class Person:
    name = "Anonymous"

    def changeName(self, name):
        self.__class__.name = name 
"""


class Person:
    name = "Anonymous"
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Laiba Khan Yousufzai")
print(p1.name)
print(Person.name)

# PROPERTY DECORATOR

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3 ) + "%"

stu1 = Student(98, 97, 90)
print(stu1.percentage)

stu1.phy = 86 
print(stu1.phy) 
print(stu1.percentage)


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    # def calcPercentage(self):
    #          self.percentage = str((self.phy + self.chem + self.math) / 3 ) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3 ) + "%"
        


stu1 = Student(98, 97, 90)
print(stu1.percentage)

stu1.phy = 86 
print(stu1.phy) 
print(stu1.percentage)

# POLYMORPHISM

print(1 + 2) #3
print("artificial" + "intelligence") # concatenate
print([1,2,3] + [4,5,6]) #merge

# EXAMPLES:

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +" , self.img, "j")

num1 = Complex(1,2)
num1.showNumber()

num2 = Complex(3,4)
num2.showNumber() 


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +" , self.img, "j")

    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
num1 = Complex(1,2)
num1.showNumber()

num2 = Complex(3,4)
num2.showNumber() 

num3 = num1.add(num2)
num3.showNumber()

# print(num1 + num2) # This will throw an error. Now we use dunder function

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +" , self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
    
num1 = Complex(1,2)
num1.showNumber()

num2 = Complex(3,4)
num2.showNumber() 

num3 = num1 - num2
num3.showNumber()
