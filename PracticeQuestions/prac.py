"""
Define a circle class to create a circle with radius r using the connstructor.
Define an Area() method of the class which calculates the area of the circle.
Define a Perimeter() method of the class which calculates the perimeter of the circle.
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return (22/7) * self.radius ** 2 

    def perimeter(self):
        return 2 * (22/7) * self.radius


c = Circle(5)   
print(c.area())
print(c.radius)
print(c.perimeter())

"""
Define an Employee class with attributes role, department and salary. This class showDetails() method.
Create an Engineer class that inherits properties from Employee and Employee attributes: name and age
"""

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print(f"Role: {self.role}, Department: {self.dept}, Salary: {self.salary}")

class Engineer(Employee):
    def __init__(self, name, age):
        super().__init__("Engineer", "IT", "90000")
        self.name = name
        self.age = age

eng1 = Engineer("Elon", "28")
eng1.showDetails()

"""
Create a class called Order which stores item and its price.
Use Dunder function __gt__() to convey that:
order1>order2 if price of order1 > price of order2
"""

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price
    
odr1 = Order("juice", 30)
odr2 = Order("Jamboo Roll", 200)

print(odr1 > odr2)