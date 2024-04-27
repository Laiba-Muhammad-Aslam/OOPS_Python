# EXAMPLE 

# MY SOLUTION

class Student:
    def __init__(self, name, subj1, subj2, subj3):
        self.name = name
        self.subj1 = subj1
        self.subj2 = subj2
        self.subj3 = subj3
        
    def avgOfmarks(self):
        avg = (self.subj1 + self.subj2 + self.subj3) / 3
        print(avg)
    
s1 = Student("Rahul", 100,98,90)
s1.avgOfmarks()

s2 = Student("Zobia",10,9,90)
s2.avgOfmarks()

# VIDEO SOLUTION:

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your avg score is:", sum/3)
    
s1 = Student("Laiba", [100, 99, 90])
s1.get_avg()

# ABSTRACTION EXAMPLE

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.acc = True
        self.clutch = True
        print("Car Started....")

car1 = Car()
car1.start()        
        
# BANK ACCOUNT EXAMPLE 

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total Balance = ", self.get_balance())
        
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total Balance = ", self.get_balance())
    
    def get_balance(self):
        return self.balance
    
    
acc1 = Account(10000, 12345)
# print(acc1.balance)
# print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)