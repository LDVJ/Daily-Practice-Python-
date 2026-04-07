def format_name(name: str) -> str:
    name_lst = name.split()
    output = []
    for word in name_lst:
        update = word[0].upper() + word[1:]
        output.append(update)
    return " ".join(output)

def calculate_average(marks : list) -> float:
    sum = 0
    for num in marks:
        sum += num
    
    avg = sum/len(marks)
    return avg

def get_grade(avg: float) -> str:
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"
    
def student_summary(name : str, marks: list, grade : str ,course : str = "Python Basics"):
    print(f"""Summary of student : {name}
        First Marks : {marks[0]}
        Middle Part : {marks[1:-1]}""")
    for key, value in enumerate(marks):
        print(f"Marks{[key]} : {value}")
    student_info = (name, course, grade)
    return student_info

name = input("Enter your name: ")
try:
    marks = [int(x) for x in input("Enter your value: ").split()]
except ValueError:
    print("Invalid Value")

formatted_name = format_name(name=name)
average_marks = calculate_average(marks=marks)
grade_got = get_grade(avg=average_marks)
print(student_summary(name=formatted_name, marks=marks, grade=grade_got,))
