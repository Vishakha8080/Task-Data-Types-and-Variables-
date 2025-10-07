name = "Aditya" 
age = 19           
test_score = 93.2

print("Name:", name)
print("Age:", age)
print("Test Score:", test_score)


first_name = "Aditya"
last_name = "Jain"

full_name = first_name + " " + last_name

print("Full Name:", full_name)


fruits = ["Apple", "Pineapple", "Mango", "Orange", "Kiwi"]

print("First fruit:", fruits[0])    
print("Second fruit:", fruits[1])    
print("Last fruit:", fruits[-1])    

print("All fruits:", fruits)

numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)

celsius = float(input("Enter temperature in Celsius: "))
kelvin = celsius + 273.15
print("Temperature in Kelvin:", kelvin)

text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

def reverse_string(s):
    return s[::-1]

string = input("Enter a string: ")
print("Reversed string:", reverse_string(string))

names = ["Aditya", "Ayush", "Krushna"]
result = " ".join(names)
print("Concatenated string:", result)

import math

radius = float(input("Enter the radius: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print("Area:", area)
print("Circumference:", circumference)

minutes = int(input("Enter number of minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60

print(f"{minutes} minutes = {hours} hour(s) and {remaining_minutes} minute(s)")

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(s.lower())

text = input("Enter a string: ")
if is_pangram(text):
    print("It is a pangram.")
else:
    print("Not a pangram.")


    year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

    numbers = [10, 15, 22, 33, 42, 55, 60]
even_numbers = [num for num in numbers if num % 2 == 0]

print("Original list:", numbers)
print("Even numbers:", even_numbers)


num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")


    names = ["Alice", "Bob", "Anita", "Charlie", "Arjun", "David"]

a_names = [name for name in names if name.startswith('A')]

print("Names starting with A:", a_names)


num = int(input("Enter a number: "))

print(f"Multiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


    num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is", factorial)


    print("Prime numbers between 1 and 50 are:")
for num in range(2, 51):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")


        words = ["apple", "banana", "cherry", "mango", "strawberry", "grape"]
count = 0

for word in words:
    if len(word) > 5:
        count += 1

print("Number of words with more than 5 characters:", count)


num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits =", total)



n_terms = 100  

a, b = 0, 1  

print("Fibonacci sequence up to", n_terms, "terms:")

for i in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b


