# Program to merge two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)


# Program to find the most frequent element in a list
numbers = [1, 3, 2, 1, 4, 1, 3, 2, 1]
most_frequent = max(set(numbers), key=numbers.count)
print("Most frequent element:", most_frequent)


# Function to remove a key-value pair
def remove_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary

student = {'name': 'Divya', 'age': 23, 'city': 'Banglore'}
print(remove_key(student, 'city'))


# Program to check if two sets have any elements in common
set1 = {1, 2, 3}
set2 = {3, 4, 5}

common = set1 & set2
if common:
    print("Common elements:", common)
else:
    print("No common elements")


# Find dictionary with highest value for a specific key
data = [
    {'name': 'Malhar', 'score': 88},
    {'name': 'Manasvi', 'score': 95},
    {'name': 'Khushi', 'score': 91}
]

highest = max(data, key=lambda x: x['score'])
print("Highest score dictionary:", highest)

# Count occurrences of each character
text = "pythonprogram"
char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1

print("Character count:", char_count)



# Union, intersection, and difference
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)


# Sort list of dictionaries by key
students = [
    {'name': 'Malhar', 'age': 21},
    {'name': 'Manasvi', 'age': 19},
    {'name': 'Khushi', 'age': 22}
]

sorted_students = sorted(students, key=lambda x: x['age'])
print("Sorted by age:", sorted_students)


# Find average value for a specific key
records = [
    {'name': 'Malhar', 'marks': 80},
    {'name': 'Manasvi', 'marks': 90},
    {'name': 'Khushi', 'marks': 70}
]

average = sum(d['marks'] for d in records) / len(records)
print("Average marks:", average)


# Unique characters common in all strings
strings = ["python", "typhoon", "phony"]

common_chars = set(strings[0])
for s in strings[1:]:
    common_chars &= set(s)

print("Common unique characters:", common_chars)





