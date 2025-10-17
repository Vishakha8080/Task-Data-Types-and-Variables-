import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

c = Circle(5)
print("Circle area:", c.area())
print("Circle perimeter:", c.perimeter())

s = Square(4)
print("Square area:", s.area())
print("Square perimeter:", s.perimeter())

################################################################################

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Engineer(Employee):
    def __init__(self, name, salary, skill):
        super().__init__(name, salary)
        self.skill = skill

m = Manager("Alice", 80000, "HR")
e = Engineer("Bob", 60000, "Python")

print(m.name, m.department)
print(e.name, e.skill)

################################################################################

class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

t = Triangle(10, 5)
r = Rectangle(4, 6)

print("Triangle area:", t.area())
print("Rectangle area:", r.area())

################################################################################

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Bird(Animal):
    def sound(self):
        return "Chirp!"

class Fish(Animal):
    def sound(self):
        return "Blub!"

b = Bird("Sparrow")
f = Fish("Goldfish")

print(b.name, "sound:", b.sound())
print(f.name, "sound:", f.sound())

################################################################################

import json

class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def display(self):
        print(f"Product: {self.__name}, Price: {self.__price}, Quantity: {self.__quantity}")

# Sample JSON
data = '''
[
    {"name": "Pen", "price": 10, "quantity": 100},
    {"name": "Book", "price": 50, "quantity": 30}
]
'''

products = json.loads(data)
for p in products:
    obj = Product(p['name'], p['price'], p['quantity'])
    obj.display()

################################################################################

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def drive(self):
        return f"{self.brand} car is driving"

class Bike(Vehicle):
    def drive(self):
        return f"{self.brand} bike is racing"

class Truck(Vehicle):
    def drive(self):
        return f"{self.brand} truck is carrying goods"

c = Car("Toyota")
b = Bike("Yamaha")
t = Truck("Tata")

print(c.drive())
print(b.drive())
print(t.drive())

################################################################################

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # private

    def display_user(self):
        print(f"Username: {self.username}")

    def check_password(self, pwd):
        if self.__password == pwd:
            print("Access Granted")
        else:
            print("Access Denied")

u = User("Vish", "mypassword")
u.display_user()
u.check_password("mypassword")

################################################################################

class Electronics:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

class Phone(Electronics):
    def __init__(self, brand, price, camera):
        super().__init__(brand, price)
        self.camera = camera

class Laptop(Electronics):
    def __init__(self, brand, price, ram):
        super().__init__(brand, price)
        self.ram = ram

p = Phone("Samsung", 25000, "48MP")
l = Laptop("HP", 60000, "16GB")

print(p.brand, p.camera)
print(l.brand, l.ram)

################################################################################

import csv

class Employee:
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def show_details(self):
        print(f"Name: {self.__name}, Position: {self.__position}, Salary: {self.__salary}")

with open("employees.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        emp = Employee(row['name'], row['position'], row['salary'])
        emp.show_details()

################################################################################

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

shapes = [Circle(5), Triangle(10, 5), Rectangle(4, 6)]

for s in shapes:
    print("Area:", s.area())

################################################################################
