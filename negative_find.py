li = []

try:
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        value = int(input("Enter integer values for list: "))
        li.append(value)
    for num in li:
        if num < 0:
            print("First Negative number: ", num)
            break
    else:
        print("No negative values.")

except ValueError:
    print("Invalid Value")