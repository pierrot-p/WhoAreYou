from flask import (
    Flask,
    flash,
    render_template,
    request,
    redirect,
)

from werkzeug.utils import secure_filename
import os
import os.path
import cv2
from deepface import DeepFace

app = Flask(__name__)

app.secret_key = "super secret key"

UPLOAD_FOLDER = "./static/"
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            img = cv2.imread(os.path.join(UPLOAD_FOLDER, filename))
            predictions = DeepFace.analyze(img, enforce_detection=False)
            dominant_emotion = predictions["dominant_emotion"]
            dominant_race = predictions["dominant_race"]
            dominant_age = predictions["age"]
            dominant_gender = predictions["gender"]
            return render_template(
                "results.html",
                source=filename,
                stats=predictions,
                dominant_emotion=dominant_emotion,
                dominant_race=dominant_race,
                dominant_gender=dominant_gender,
                dominant_age=dominant_age,
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
