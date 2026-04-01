correct_pin = "1234"
balance = 5000

try:
    for i in range(3):
        pin = input("Enter your pin: ")
        if pin == correct_pin:
            print("Access Granted. Enter the amount of widthrawl.")
            amount = int(input("Enter the amount: "))
            if amount <= balance:
                print("Balance Remainin: ", balance-amount)
                print("Amount withdrawal: ", amount, "\n", "Thankyou for using Smart ATM")
                break
            elif amount == 0:
                print("Thank you for using Smart Atm")
                break
            else:
                print("Insufficient Balance.")
        else:
            print("Incorrect Pin")
except ValueError:
    print("Invalid Value")