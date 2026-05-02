from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "user_uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Home route
@app.route("/")
def home_page():
    return render_template("index.html")


# Create route
@app.route("/create", methods=["GET", "POST"])
def create_page():
    myId = str(uuid.uuid4())

    if request.method == "POST":
        rec_id = request.form.get("uuid") or str(uuid.uuid4())
        desc = request.form.get("text")

        upload_path = os.path.join(app.config["UPLOAD_FOLDER"], rec_id)
        os.makedirs(upload_path, exist_ok=True)

        for key in request.files:
            file = request.files[key]
            if file and file.filename:
                filename = secure_filename(file.filename)
                file.save(os.path.join(upload_path, filename))

        with open(os.path.join(upload_path, "desc.txt"), "w") as f:
            f.write(desc or "")

    return render_template("create.html", myId=myId)


# Gallery route
@app.route("/gallery")
def gallery_page():
    return render_template("gallery.html")


if __name__ == "__main__":
    app.run(debug=True)
