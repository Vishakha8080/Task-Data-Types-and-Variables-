# Program to copy contents of one text file to another
with open("source.txt", "r") as src:
    content = src.read()

with open("destination.txt", "w") as dest:
    dest.write(content)

print("File copied successfully!")

############################################################################

import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    top_student = max(reader, key=lambda x: int(x["score"]))

print("Top student:", top_student["name"], "with score", top_student["score"])

############################################################################

with open("sample.txt", "r") as file:
    lines = file.readlines()

num_lines = len(lines)
num_words = sum(len(line.split()) for line in lines)

print("Lines:", num_lines)
print("Words:", num_words)

############################################################################

def write_sentences(sentences, filename):
    with open(filename, "w") as f:
        for sentence in sentences:
            f.write(sentence + "\n")

sentences = ["Python is fun.", "File handling is easy.", "Practice makes perfect."]
write_sentences(sentences, "sentences.txt")
print("Sentences written to file.")

############################################################################

import csv

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    salaries = [int(row["salary"]) for row in reader]

average_salary = sum(salaries) / len(salaries)
print("Average salary:", average_salary)

############################################################################

import csv

product_name = "Pen"
total_revenue = 0

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["product"] == product_name:
            total_revenue += int(row["quantity"]) * int(row["price"])

print(f"Total revenue for {product_name}: {total_revenue}")

############################################################################

def sum_numbers(filename):
    with open(filename, "r") as f:
        return sum(int(line.strip()) for line in f)

print("Sum of numbers:", sum_numbers("numbers.txt"))

############################################################################


import csv
import matplotlib.pyplot as plt

products, sales = [], []

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        products.append(row["product"])
        sales.append(int(row["sales"]))

plt.bar(products, sales)
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Sales Data")
plt.show()

############################################################################

import json

with open("data.json", "r") as file:
    data = json.load(file)

print("Name:", data["name"])
print("City:", data["city"])

############################################################################

import csv

temps = []

with open("temperature.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        temps.append(int(row["temp"]))

average_temp = sum(temps) / len(temps)
print("Average temperature:", average_temp)
