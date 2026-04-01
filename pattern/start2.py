try:
    n = int(input("Enter your Value: "))
    for i in range(1,n+1):
        print((" "*(n-i)) + ("*"*i))

except ValueError:
    print("Invalid Value.")