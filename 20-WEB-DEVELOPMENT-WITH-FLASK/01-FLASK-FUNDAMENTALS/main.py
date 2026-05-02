from flask import Flask, render_template, request

# Initialize the Flask application
# static_url_path changes the URL path for static files
app = Flask(__name__, static_url_path="/public")
# app = Flask(__name__, static_folder="assets")  # Alternative way to change static folder


# Home route
@app.route("/")
def home_page():
    return render_template("home.html")


# Services route
@app.route("/services")
def services_page():
    return render_template("services.html")


# Contact route (handles both GET and POST requests)
@app.route("/contact", methods=["GET", "POST"])
def contact_page():

    if request.method == "POST":
        # Get form data safely
        user_name = request.form.get("name")
        user_email = request.form.get("email")

        # Save form data to a file
        with open("contact_data.txt", "a", encoding="utf-8") as file_handle:
            file_handle.write(f"Name: {user_name}, Email: {user_email}\n")

        # Render the same page after submission
        return render_template("contact.html")

    # Handle GET request
    return render_template("contact.html")


# About route
@app.route("/about")
def about_page():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
