a = input("Enter your Divident: ")
b = input("Enter you Divisor: ")

try:
    a = int(a); b = int(b)
    if a == 0 and b != 0:
        print("Output", 0)
    elif b == 0:
        print("Output", "Undefined")
    else:
        div = a / b
        print("Output", round(div,2))

except ValueError:
    print("Invalid input")