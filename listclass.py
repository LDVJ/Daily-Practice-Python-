tasks = []

while True:
    action = input("What action you want to perform, Add, Remove, quit, view: ")

    if action.lower() == "add":
        value = input("Value: ")
        tasks.append(value)
        print(f"Your Value {value} is added")
        continue
    elif action.lower() == "remove":
        value = input("Value: ")
        tasks.remove(value)
        print(f"Your Value {value} is added")
        continue
    elif action.lower() == "view":
        print(tasks)
        continue
    elif action.lower() == "quit":
        print("Thanks for using this system")
        break
    else: 
        print("Undefined Method")
        continue