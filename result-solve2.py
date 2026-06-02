student_data = [
    ("Aarav", 20, [80, 70, 90]),
    ("Meera", 17, [45, 55]),
    ("Kabir", 19, [])
]


class Person:
    total_people = 0
    def __init__(self, name, age):
        self.name =name
        self.age = age
        Person.total_people += 1

    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True  
        return False
    
    @classmethod
    def get_total_people(cls):
        return cls.total_people
    
    def display(self):
        return f"Name: {self.name}, Age: {self.age}"
    
class Student(Person):
    def __init__(self, name, age, scores = None):
        super().__init__(name,age)
        if scores == None:
            self.scores = []
        else:
            self.scores = scores
    
    def average_Score(self):
        if self.scores == []:
            return 0
        else:
            total = sum(self.scores)
            average = total/ len(self.scores)

            return average

    def display(self):
        return f"{self.name} ({self.age}) - Average: {self.average_Score():.2f} - Adult: {'Yes' if Person.is_adult(self.age) else 'No'}"

for student in student_data:
    student_name, student_age, student_scores = student
    student_obj = Student(name=student_name, age=student_age, scores=student_scores)

    print(student_obj.display())

print("Total People Created:",Person.get_total_people())