from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)


# Home route
@app.route("/")
def show_home_page():
    student_marks = {
        "John": 45,
        "Jane": 32,
        "Bob": 65,
        "Alice": 78,
        "Peter": 89,
        "Abhishek": 90,
        "Adarsh": 43,
        "Rahul": 78,
    }
    return render_template("index.html", data=student_marks)


# About page route
@app.route("/about")
def show_about_page():
    return render_template("about.html")


# Contact page route
@app.route("/contact")
def show_contact_page():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
