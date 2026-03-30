try:
    age = int(input("Enter your age: "))
    income =int(input("Enter your income: "))
    credit_score = int(input("Enter your credit score: "))
    if (age > 0 and income >= 0 and credit_score >= 0):
        if age >= 21 and income >= 30000 and credit_score >= 650:
            print("Eligible")
        else:
            print("Not Eligible") 
    else:
        print("Invalid")

except ValueError:
    print("Invlid Value")
