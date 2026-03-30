try:
    score = int(input("Enter your valaue: "))
    if 0 <= score <= 100:
        if score >= 90:
            print("A")
        elif score >= 80:
            print("B")
        elif score >= 70:
            print("C")
        elif score >= 60:
            print("D")
        else:
            print("F")
    else:
        print("Invalid")
except ValueError:
    print("Invalid Value")