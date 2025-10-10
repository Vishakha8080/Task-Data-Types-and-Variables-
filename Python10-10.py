def sum_of_positive(numbers):
    return sum(num for num in numbers if num > 0)

print(sum_of_positive([-4, 32, 56 , -16, 7])) 

################################################################################

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("Madam")) 

#################################################################################

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5)) 


#################################################################################

def square_list(numbers):
    return [num ** 2 for num in numbers]

print(square_list([7, 8, 9]))  

#################################################################################

def even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print(even_or_odd(5468))  

#################################################################################

def triangle_area(base, height):
    return 0.5 * base * height

print(triangle_area(25, 7))  

#################################################################################

def sort_strings(strings):
    return sorted(strings)

print(sort_strings(["Strawberry", "Chikoo", "Kiwi"]))

#################################################################################

def list_intersection(list1, list2):
    return list(set(list1) & set(list2))

print(list_intersection([1, 8, 9], [8, 9, 4]))  

#################################################################################

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap_year(2024))  

#################################################################################

def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

multiplication_table(7)
