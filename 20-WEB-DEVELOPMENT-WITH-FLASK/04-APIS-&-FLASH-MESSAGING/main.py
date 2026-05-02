from flask import Flask, jsonify, flash, render_template

app = Flask(__name__)

# Secret key is required to use flash messages
app.secret_key = "super_secret_key"


# Dictionary storing student names and their marks
student_marks_data = {
    "Soumen": 45,
    "Mousumi": 32,
    "Subhajit": 65,
    "Ananya": 78,
    "Arindam": 89,
    "Debasish": 90,
}


# Convert dictionary into a list of student records
student_records = [
    {"name": student_name, "marks": marks_obtained}
    for student_name, marks_obtained in student_marks_data.items()
]


# Prepare API response
api_response = {
    "status": "success",
    "data": {"students": student_records, "total_students": len(student_records)},
}


# Home route: returns student data in JSON format
@app.route("/")
def get_student_data():
    return jsonify(api_response)


# About route: displays a flash message
@app.route("/about")
def show_about_page():
    flash("You are currently on the About page.")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
