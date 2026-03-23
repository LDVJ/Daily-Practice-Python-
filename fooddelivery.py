items = int(input("Enter the number of Items: "))
price = float(input("Enter the price: "))

if items >= 0 and price >= 0:
    total = items*price
    print(f"Total Price: {total:.2f}")
else:
    print("Invalid Input")