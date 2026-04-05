email = input("Enter your Email: ").strip()

check = {"@":0,".":0}

def check_repitition(email : str) -> bool:
    for value in email:
        if value == "@":
            check["@"] = check["@"] + 1
        if value == ".": 
            check["."] = check["."] + 1

    return (check.get("@") == 1 and check.get(".") == 1)

if len(email) < 9:
    print("Email Length is too short to be valid")

elif (("@" in email) and ("." in email) and (not (" " in email)) and (not email.startswith("@")) and (not email.startswith(".")) and check_repitition(email=email)):
    print("Valid Email")

else:
    print("Invalid Email")