try:
    value = int(input("Enter the value: "))
    if value > 0:
        for i  in range(1,11):
            print(f"{value} * {i} = {i *value}")
    else:
        print("Value should be greater than 0.")
except ValueError:
    print("Invalid Value")