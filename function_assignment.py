"""Build a Small Function-Based Utility Program
Write a Python program using functions to do the following:

Requirements
Create a function show_menu() that prints:

Add Numbers
Greet User
Check Number Type
Create a function add_numbers(a, b) that:

takes two numbers as parameters
returns their sum
Create a function greet_user(name, greeting="Hello") that:

uses a default parameter
returns a greeting message using an f-string
Create a function check_number(num) that:

returns:
"Positive" if number > 0
"Negative" if number < 0
"Zero" otherwise
Call all functions in your program and print meaningful outputs.

"""
def add_numbers(a : int, b : int) -> int:
    return a + b

def greet_user(name : str , greeting : str = "Hello") -> str:
    return f"{greeting}, {name}!"

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def make_email(username: str, domain : str = "gmail.com") -> str:
    return f"{username}@{domain}"

def show_menu():

    print("1. Add Numbers")
    print("2. Greet User")
    print("3. Check Number Type",end="\n\n")

    print("Sum:",add_numbers(2,3))
    print(greet_user(name="Lucky"))
    print(check_number(num=-3))
    print(make_email(username="testing"))

    
show_menu()
