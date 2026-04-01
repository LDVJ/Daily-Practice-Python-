try:
    n = int(input("Enter your value: "))
    for i in range(1,n+1):
        print(str(i)*i)
except ValueError:
    print("Invalid Value")