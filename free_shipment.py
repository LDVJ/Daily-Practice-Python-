try:
    price = float(input("Enter price: ").strip())
    premium_input = input("Enter if premium (True/False): ").strip().lower()

    if premium_input == "true":
        is_premium = True
    elif premium_input == "false":
        is_premium = False
    else:
        print("Invalaid premium input")
        exit()

    if not price < 0:
        if price > 50 or is_premium:
            print("Free Shipping")
        else:
            print("Shipping Charges Apply.")
    else:
        print("Invalid price")

except ValueError:
    print("Invalid Value")