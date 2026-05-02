from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home_page():
    # Default values (used if no query parameters are provided)
    user_name = "Soumadip Majila"
    user_token = 67000

    # Read query parameters from the URL
    # Example: http://127.0.0.1:5000/?name=John&token=123

    if "name" in request.args:
        user_name = request.args.get("name")

    if "token" in request.args:
        user_token = request.args.get("token")

    return render_template("index.html", name=user_name, token=user_token)


if __name__ == "__main__":
    app.run(debug=True)
