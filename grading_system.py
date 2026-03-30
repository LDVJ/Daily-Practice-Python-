"""Problem Statement

Write a Python program that performs the following tasks:

Take student name as input.
Take student marks (integer) as input.
Take attendance percentage as input.
Assign grade using conditionals:
Marks ≥ 90 → Grade A
Marks ≥ 75 → Grade B
Marks ≥ 50 → Grade C
Otherwise → Fail
Determine scholarship eligibility using nested conditionals:
Student must NOT fail.
Attendance must be greater than 80.
Display output in this format:

Hello name

Grade: grade

Scholarship Eligible: True/False

"""
name = input("Enter your name: ")

try:
    marks = int(input(f"Enter student {name} marks: "))
    attendance  = float(input(f"Enter student {name} attendence: "))
    print(f"Hello {name}",end= "\n\n")

    if marks > 100 or marks < 0:
        print("Invalid Marks. Marks must be between 0 and 100.")
    elif attendance > 100 or attendance < 0:
        print("Invalid attendance. Attendance must be between 0 and 100.")
    else:
        if marks >=  90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        else: 
            grade = "Fail"
        
        if grade != "Fail" and attendance > 80:
            print(f"Grade: {grade}", end="\n\n")
            print(f"Scholarship Eligible: True")
        else:
            print(f"Grade: {grade}", end="\n\n")
            print(f"Scholarship Eligible: False")


except ValueError:
    print("Invalid Values.")