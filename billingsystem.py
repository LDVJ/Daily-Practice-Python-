item = input("Enter your Item: ")
quantity = input("Enter the quantity: ")
price = input("Enter price: ")

try:
    quant = int(quantity)
    price = float(quantity)
    if quant < 0 or price < 0:
        print("Invalid Input")
    else:
        total = quantity*price
        print(f"Item: {item}")
        print(f"Total: {total}")


except ValueError:
    print("Invalid Input")