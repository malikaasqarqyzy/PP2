import math

# 1. Define a class which has at least two methods
# getString: to get a string from console input 
# printString: to print the string in upper case.

class Class:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("Uppercase string:", self.input_string.upper())

result = Class()
Class.getString()
Class.printString()

# 2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape():
    area = 0
    class Square():
        def __init__(self, length):
            self.length = int(input())
            
# 3. Define a class named Rectangle which inherits from Shape class from task 2. 
# Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.

class Rectangle(object):
    def __init__(self, l : int, w : int) -> None:
        self.length = l
        self.width  = w

    def area(self):
        return self.length * self.width
    
length = int(input())
width = int(input())
result = Rectangle(length, width)
print(result.area())

# 4. Write the definition of a Point class. Objects from this class should have a
# a method show to display the coordinates of the point
# a method move to change these coordinates
# a method dist that computes the distance between 2 points

class Point(object):
    def __init__(self, x : float, y : float) -> None:
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x : float, y : float):
        self.x += x
        self.y += y

    def dist(self, pt):
        dx = pt.x - self.x
        dy = pt.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)

#5 Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
# Withdrawals may not exceed the available balance. 
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        amount <= self.balance
        self.balance -= amount

#6 Write a program which can filter prime numbers in a list by using filter function. 
# Note: Use lambda to define anonymous functions.

def prime (lst):
    result = lst
    for i in range(2, max(lst) // 2 + 1):
        result = filter(lambda x: x == i or x % i, result)
    return list(result)
lst = [int(x) for x in input().split()]
print(prime(lst))
