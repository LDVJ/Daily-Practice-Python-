import random

our_num = random.randint(1,100)

print("Welcome to Guesing Game")

attempt = 0

while True:
    if attempt < 5:
        user_num = input("Enter your number: ")
        try:
            user_num = int(user_num)
            if user_num > our_num:
                print("Choose something smaller bro")
            elif user_num < our_num:
                print("Choose something higher bro")
            else:
                print("Bro You Won")
                break
            attempt += 1
        except ValueError:
            print("Invalid Number.")
            user_num = input("Enter your number: ")
    else:
        print("You are out of attempts better luck next time.")
        print(f"Actual Number: {our_num}")
        break
