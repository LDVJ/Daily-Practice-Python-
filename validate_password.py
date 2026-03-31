import re

# pattern = r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,}$"

while True:
    password = input("Enter your password: ").strip()
    num = "0987654321"
    has_number = False
    for i in range(len(num)):
        if num[i] in password:
            has_number = True

    if len(password) >= 8 and has_number:
        print("Password Accepted.")
        break
    else:
        if len(password) < 8:
            print("Too Short!")
        if not has_number:
            print("Must contain a digit!")
        