input1 = input("Enter 1st Input: ")
input2 = input("Enter 2nd Input: ")

try:
    input1 = float(input1)
    input2 = float(input2)
    print("Output: ", input1+input2)
except ValueError:
    print("Invalid action")
