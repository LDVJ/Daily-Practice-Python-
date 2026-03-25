name = input('Enter your name: ').strip()
age = input("Enter your age: ")
mark1 = input("Enter mark1 score: ")
mark2 = input("Enter mark2 score: ")

if name:
    try:
        age = int(age)
        mark1 = int(mark1)
        mark2 = int(mark2)
        if age <= 0 or mark1 < 0 or mark1 > 100 or mark2 > 100 or mark2 < 0:
            print("Invalid Input")
        else:
            total = mark1 + mark2
            average = total/2
            print(f"Hello {name}")
            print(f"Age next year: {age + 1}")
            print(f"Total Marks: {total}")
            print(f"Average Marks: {average:.2f}")
            print(f"Eligible for Scholarship: {average > 75 and age < 25}")

    except ValueError:
        print("Invalid Input")

else:
    print("Invalid Name")