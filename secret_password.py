max_attempts = 3
correct_password = "Python123"
attempt = 0

# while True:
#     if attempt < 3:
#         password = input("Enter your Password: ")
#         if password == correct_password:
#             print("Access Granted!")
#             break
#         elif password == "Skip" and attempt < 2:
#             attempt += 1
#             continue
#         elif attempt < 2:
#             print("Wrong Password. Try Again")
#             attempt += 1
#             continue
#         else:
#             print("System Locked")
#             break

for attempt in range(max_attempts):
    password = input("Enter your Paswword: ").strip()
    if password == correct_password:
        print("Access Granted!")
        break
    elif password == "Skip" and attempt < 2:
        continue
    elif attempt <2: 
        print("Wrong Password. Try Again")
        continue
    elif attempt == 2:
        print("Wrong Password")
        print("System Locked")
    else:
        print("System Locked")
        break