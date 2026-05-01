from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        with open("file.txt", "a") as f:
            f.write(f"name: {name}, email: {email} \n")

        return render_template("contact.html")

    return render_template("contact.html")


@app.route("/about")
def about():

    return render_template("about.html")


app.run(port=8080, debug=True)
