# Given two lists of numbers, concatenate them into a single list
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2
print("Concatenated list:", result)


# Write a program that finds the largest and smallest elements in a list
numbers = [10, 5, 25, 8, 30]

largest = max(numbers)
smallest = min(numbers)

print("Largest element:", largest)
print("Smallest element:", smallest)


# Implement a function that takes a list of numbers and returns a new list with squared values
def square_list(numbers):
    return [x**2 for x in numbers]

nums = [2, 3, 4, 5]
result = square_list(nums)
print("Squared list:", result)


# Create a program that finds the common elements between two lists and stores them in a new list
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = [x for x in list1 if x in list2]
print("Common elements:", common)


# Given a list of words, find the word with the maximum length and its length
words = ["apple", "banana", "grapefruit", "kiwi"]

longest_word = max(words, key=len)
print("Longest word:", longest_word)
print("Length:", len(longest_word))


# Write a Python program to count the occurrences of each element in a given list
items = ['a', 'b', 'a', 'c', 'b', 'a']

counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1

print("Occurrences:", counts)



# Given a list of names, remove all duplicate names and print the unique names
names = ["Aditya", "Ayush", "Aditya", "Krushna", "Ayush"]

unique_names = list(set(names))
print("Unique names:", unique_names)


# Create a function that takes a list of strings and returns the list sorted by length
def sort_by_length(strings):
    return sorted(strings, key=len)

words = ["apple", "kiwi", "banana", "Custurdapple"]
sorted_list = sort_by_length(words)
print("Sorted by length:", sorted_list)


# Write a program that checks if a given list is sorted in ascending order
def is_sorted(lst):
    return lst == sorted(lst)

nums = [1, 2, 3, 4, 5]
print("Is list sorted?", is_sorted(nums))


# Implement a function that takes two lists and returns their union (all unique elements)
def union_lists(list1, list2):
    return list(set(list1) | set(list2))

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
result = union_lists(a, b)
print("Union of lists:", result)

