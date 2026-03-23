username = input("Enter your username: ").strip()
age = input("Ener your age: ")

if not username:
    print("Invalid Username")
else:
    try:
        age = int(age)
        if age < 0:
            print("Invalid age")
        elif age < 18:
            print("Not Allowed")
        else:
            print(f"Welcome, {username}")
    except ValueError:
        print("Invalid Age")