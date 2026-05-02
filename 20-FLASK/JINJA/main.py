from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def hello_world():
  marks={
    "John": 45,
    "Jane": 32,
    "Bob": 65,
    "Alice": 78,
    "Peter": 89,
    "Abhishek": 90,
    "Adarsh": 43,
    "Rahul": 78
  }
  return render_template("index.html", data=marks)


@app.route("/about")
def about():
  return render_template("about.html")


@app.route("/contact")
def contact():
  return render_template("contact.html")




app.run(debug=True)