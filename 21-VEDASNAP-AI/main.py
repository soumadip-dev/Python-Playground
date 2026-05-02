from flask import Flask, render_template

app = Flask(__name__)


# Home route
@app.route("/")
def home_page():
    return render_template("index.html")


# Create route
@app.route("/create")
def create_page():
    return render_template("create.html")


# Gallery route
@app.route("/gallery")
def gallery_page():
    return render_template("gallery.html")


if __name__ == "__main__":
    app.run(debug=True)
