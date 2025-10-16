class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

student1 = Student("Saee", 25, [85, 90, 88])
student1.display_info()

############################################################################

import csv

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display(self):
        print(f"{self.name} - {self.position} - ₹{self.salary}")


with open("employees.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        emp = Employee(row["name"], row["position"], row["salary"])
        emp.display()
        
############################################################################

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")
        else:
            print("Insufficient funds!")


acc = BankAccount("Vishakha", 5000)
acc.deposit(1500)
acc.withdraw(2000)

############################################################################

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(5, 3)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

############################################################################

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"{self.year} {self.make} {self.model}")

car1 = Car("Toyota", "Fortuner", 2023)
car1.display()

############################################################################

import json

class Customer:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def display(self):
        print(f"{self.name} ({self.age}) - {self.email}")

with open("customers.json") as file:
    data = json.load(file)
    for item in data:
        customer = Customer(item["name"], item["email"], item["age"])
        customer.display()

############################################################################

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

person1 = Person("Sujeet", 22, "Pune, India")
person1.show()

############################################################################

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

circles = [Circle(3), Circle(5), Circle(7)]
for c in circles:
    print(f"Radius: {c.radius}, Area: {c.area():.2f}, Circumference: {c.circumference():.2f}")

############################################################################

import csv

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def total_value(self):
        return self.price * self.quantity

with open("products.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        prod = Product(row["name"], row["price"], row["quantity"])
        print(f"{prod.name} - ₹{prod.price} x {prod.quantity} = ₹{prod.total_value()}")

############################################################################

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def show(self):
        print(f"🎬 {self.title} by {self.director} - Rating: {self.rating}/10")

movie1 = Movie("Inception", "Christopher Nolan", 9)
movie1.show()

############################################################################

