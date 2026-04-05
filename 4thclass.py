# Function - set of instructions that performs a particular operation.
# Functions introduces reusability and abstraction.

# DRY Principle - Don't Repeat Yourself
# abstraction - hiding unnecessary details from the client.
# functions helps us to make our code modular.

# Functions - Subroutines (Long Back ~1960-70)

# functions - define once and reuse many times.

# function definition
def say_hello():
    print("Hello World")

def say_bye():
    print("Bye World")

def say_hi():
    print("Hi Everyone")

# say_hello() # function calling.

# def : defines a function
# function name
# parentheses.
# parameters
# colon - Start of the function unit.

def show_header():
    print("=" * 20)
    print("Welcome to Masai Class.")
    print("=" * 20)

def show_content():
    print("This is the class on Python functions.")

def show_footer():
    print("=" * 20)
    print("Thans for attending the class.")
    print("=" * 20)

def show_entire_content():
    show_header()
    show_content()
    show_footer()

# A function can call other functions too.

# Function Parameters - Input to the functions.
# function parameters introduces flexibility and generalization to the functions, they transforms the function from a single-purpose tool into versatile and more resuable component that works for different types of input.

# Function Parameters solves the rigidity problem: 
# function without parameters can only do one specific thing with hardcoded values.

# x: int => Type Hinting
def calculate(x: int, y: int, oprn: str = "+"): # oprn - default value is +
    if oprn == '+':
        return x + y
    elif oprn == '-':
        return x - y
    elif oprn == '*':
        return x * y
    elif oprn == '/':
        return x / y
    else:
        raise TypeError(f"{oprn} operation is not supported.")

# Parameter vs Argument

def say_hello(name: str): # parameter - name
    print(f"Hello {name}")

# say_hello("Ravneet") # argument - "Ravneet"

# Parameter - Variable in function definition.
# Argument - actual value passed at the time of calling the function.

# calculate(10, 2, '&')

# Order matters in function parameters.
# def introduce(name: str, age: int):
#     if type(name) != str or type(age) != int:
#         raise TypeError('Please pass name as string and age as integer')
#     print(f"My name is {name} and age is {age}")
    

# introduce(30, 'Deepak')

# Multiple parameters: separated by comma.

# Return Values from function
# return statement is used to return some value from the function

# def fun():
#     return 10 # return statement means function termination.
#     print("Hello World")

# print(fun() + 13)

# return vs print
# print() => prints on the console, no return value.
# return => sends some value back to caller

# Return value enables the composition.

# def fun1():
#     return 10

# def fun2():
#     return 2

# def add(x, y):
#     return x / y

# function1(function2(function3(function4()))) function composition

# function1 -> function2 -> function3 -> function4

# Can we have multiple return statements inside a function ? YES

# def fun():
#     return 10
#     return 20 # orphan

# print(fun())

# return - sends some value back to the caller, it stops the execution immediately.

# Default parameters.

# print(calculate(10, 2, '/'))

def create_user(name, age, role="student", address="India"):
    print(f"name: {name}, age: {age}, role: {role}, address: {address}")

# create_user("Deepak", 30, "Mentor")

def add_item(item, items = None): # Mutable default - Bad approach 
    if items == None:
        items = []
    items.append(item)
    print(items)

add_item('Keyboard')

add_item('Mouse')

add_item('Laptop')

add_item('Camera')