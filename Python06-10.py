
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
