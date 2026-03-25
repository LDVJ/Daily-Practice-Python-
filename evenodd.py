num = input("Enter your number: ")

try:
    num = float(num)  
    print(num)
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Invalid Input")

