try:
    count = 0
    while True:
        value = input("Enter your number: ")
        if value.lower() == "done":
            print("Output: ", count)
            break
        else:
            count += int(value)
except ValueError:
    print("Invalid Value")