from flask import Flask, jsonify
from studenttypes import Student
from studentinfo import StudentsData
app = Flask(__name__)
studentsData = StudentsData()

mark = Student(name="Mark", last_name="Jacobs", id=1)
studentsData.add_student(mark)

@app.route("/", methods=["GET"])
def students_page():
    return jsonify({"students": studentsData.get_students_data()})

if __name__ == "__main__":
    app.run(debug=True)
