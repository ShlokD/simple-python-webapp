from studenttypes import Student, HighSchoolStudent

class StudentsData:
    def __init__(self):
        self.students = [];
    def add_student(self, student: Student):
        self.students.append({
            "name": student.get_student_name(),
            "last_name": student.get_student_last_name(),
            "id": student.get_student_id(),
            "school": student.get_school_name()
        })

    def print_students_data(self):
        for student in self.students:
            student_id = student["id"]
            student_name = student["name"]
            student_school = student["school"]
            print(f"{student_id}: {student_name}, {student_school}")

    def get_students_data(self):
        return self.students


