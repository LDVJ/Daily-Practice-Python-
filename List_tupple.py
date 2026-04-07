"""Practical — String and List Operations in Python
Write a Python program that does all of the following:

Take the user's first name and last name as input
Create and print the full name using an f-string
Convert the full name to uppercase and print it
Store each character of the full name in a list using list()
Print:
First character
Last character
A slice of the first 4 characters
Create a tuple containing:
full name
length of full name
Iterate through the character list using a loop and print each character on a new line"""


first_name = input("first = ").strip()
last_name = input("last = ").strip()

full_name = f"{first_name} {last_name}"

name_lst = list(full_name)

print(f"Full Name: {full_name}")
print(f"Uppercase: {full_name.upper()}")
print(f"Character: {name_lst}")
print(f"First Character: {name_lst[0]}")
print(f"Last Character: {name_lst[-1]}")
print(f"First 4 Characters: {name_lst[:4]}")
print(f"Tuple: {(full_name,len(full_name))}")