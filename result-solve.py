students = [
    {"name": "Aarav", "scores": [72, 64, 80]},
    {"name": "Meera", "scores": [35, 42, 39]},
    {"name": "Kabir", "scores": [90, 88, 95]},
    {"name": " ", "scores": [50, 60]},
    {"name": "Tara", "scores": []}
]
try:
    def is_valid_student(record: dict) -> bool:
        if isinstance(record.get("name"), str) and record.get("name").strip() != "" and isinstance(record.get("scores"), list) and record.get("scores") != []:
            return True
        return False


    def calculate_average(scores: list) -> float:
        total = 0
        n = len(scores)
        for score in scores:
            total += score

        return total/n

    def calculate_summaries(students : list):
        output = []
        invalid_record = 0
        for student in students:
            if not is_valid_student(student):
                invalid_record += 1
                continue
            else:
                average = calculate_average(scores=student.get("scores"))

                if average >= 40:
                    status = "Pass"
                else:
                    status = "Review"
            
                summary = {
                    "name": student["name"],
                    "total" : sum(student["scores"]),
                    "average": average,
                    "status":status
                }
            output.append(summary)

        
        return output, invalid_record
    summaries, invalid_record = calculate_summaries(students)

    for student in summaries:
        print(f"""{student["name"]} - Total: {student["total"]}, Average: {student["average"]:.2f}, Status: {student["status"]}""")

    print("Invalid records Skipped:",invalid_record)

except Exception as e:
    print("Something went Wrong: ", e)