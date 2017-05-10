
class Student:
    school_name = "Springfield Elementary"
    def __init__(self, name, last_name, id):
        self.student = {"name": name, "last_name": last_name, "id": id}

    def get_student_name(self):
        return self.student.get("name", "")

    def get_student_last_name(self):
        return self.student.get("last_name", "")

    def get_student_id(self):
        return self.student.get("id", 0)

    def get_school_name(self):
        return self.school_name;

    def __str__(self):
        return f"{self.get_student_name()}"


class HighSchoolStudent(Student):
    school_name = "Springfield High"