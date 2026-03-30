username = input("Enter your username: ").strip()
password = input("Enter your password: ")

if username == "admin":
    if password == "1234":
        print("Login Successfull.")
    else:
        print("Wrong Password")
else:
    print("Username not found")
