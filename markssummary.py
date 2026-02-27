def calculate_average(marks: list) :
    temp = 0
    for i in marks:
        temp += i
    return temp/len(marks)


def count_pass_fail(marks, pass_marks=50):
    pass_count = 0
    fail_count = 0
    for i in marks:
        if i >= pass_marks:
            pass_count += 1
        else:
            fail_count += 1
    return pass_count, fail_count


def display_summary(marks: list):
    students_count = len(marks)
    avg_marks = calculate_average(marks)
    passed, failed = count_pass_fail(marks=marks)

    print("Total Students:",students_count)
    print("Average Marks:",avg_marks)
    print("Students Passed:",passed)
    print("Students Failed:",failed)


marks=[75,60,85,90,45,67,80,92]
display_summary(marks)