import pandas as pd
import matplotlib.pyplot as plt

data = {'Date': pd.date_range(start='2025-01-01', periods=10, freq='D'),
        'Sales': [100, 120, 130, 125, 140, 160, 155, 170, 180, 190]}
df = pd.DataFrame(data)

plt.plot(df['Date'], df['Sales'], marker='o')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
################################################################################

import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # Random data

plt.hist(data, bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

################################################################################

import seaborn as sns
import pandas as pd

df = sns.load_dataset('iris')
sns.pairplot(df)
plt.show()

################################################################################

import pandas as pd
import matplotlib.pyplot as plt

def create_boxplot(df):
    df.plot(kind='box', grid=True)
    plt.title('Box Plot of Data')
    plt.show()

# Example
data = {'A': [10, 20, 15, 25, 30], 'B': [5, 15, 10, 20, 25]}
df = pd.DataFrame(data)
create_boxplot(df)

################################################################################

import pandas as pd
import matplotlib.pyplot as plt

# Create CSV (run once to generate file)
data = {'Product': ['A', 'B', 'C', 'D'], 'Sales': [100, 150, 120, 180]}
df = pd.DataFrame(data)
df.to_csv('sales.csv', index=False)

# Read CSV and plot
sales_data = pd.read_csv('sales.csv')
plt.bar(sales_data['Product'], sales_data['Sales'], color='lightgreen')
plt.title('Sales Comparison by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.show()

################################################################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

# Create sample JSON
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Value': [10, 12, 20, 22, 30, 28]}
with open('data.json', 'w') as f:
    json.dump(data, f)

# Read JSON and plot
df = pd.read_json('data.json')
sns.violinplot(x='Category', y='Value', data=df)
plt.title('Violin Plot Example')
plt.show()

################################################################################

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def create_pairplot(df):
    sns.pairplot(df)
    plt.show()

# Example with Iris dataset
df = sns.load_dataset('iris')
create_pairplot(df)

################################################################################

class Electronics:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

class Phone(Electronics):
    def __init__(self, brand, price, storage):
        super().__init__(brand, price)
        self.storage = storage

class Laptop(Electronics):
    def __init__(self, brand, price, ram):
        super().__init__(brand, price)
        self.ram = ram

# Example
phone = Phone("Samsung", 50000, "128GB")
laptop = Laptop("HP", 60000, "16GB")
print(phone.__dict__)
print(laptop.__dict__)

################################################################################

import pandas as pd

# Create CSV
data = {'Name': ['Amit', 'Riya', 'Karan'],
        'Position': ['Manager', 'Developer', 'Analyst'],
        'Salary': [75000, 55000, 50000]}
df = pd.DataFrame(data)
df.to_csv('employees.csv', index=False)

# Employee class
class Employee:
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def show_details(self):
        print(f"Name: {self.__name}, Position: {self.__position}, Salary: ₹{self.__salary}")

# Read and create objects
employees = pd.read_csv('employees.csv')
for _, row in employees.iterrows():
    emp = Employee(row['Name'], row['Position'], row['Salary'])
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

# Example
shapes = [Circle(5), Triangle(10, 6), Rectangle(8, 4)]
for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.area():.2f}")


