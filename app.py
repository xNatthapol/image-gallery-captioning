import os

import requests
from dotenv import load_dotenv
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

API_URL = (
    "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
)
headers = {"Authorization": f"{API_KEY}"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads/"
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg"}


# Check if the file type is allowed
def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )


# Query the Hugging Face API for captions
def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)

    # Log the response for debugging
    print(response.json())

    response_json = response.json()
    if isinstance(response_json, list) and len(response_json) > 0:
        return response_json[0].get("generated_text", "No caption available")
    return "No caption available"


# Route to serve uploaded images
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# Index route to display the gallery
@app.route("/")
def index():
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])

    image_files = os.listdir(app.config["UPLOAD_FOLDER"])
    image_captions = {}

    for image in image_files:
        image_path = os.path.join(app.config["UPLOAD_FOLDER"], image)
        caption = query(image_path)
        image_captions[image] = caption

    return render_template("index.html", images=image_files, captions=image_captions)


# Route to handle image upload
@app.route("/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return redirect(request.url)
    file = request.files["file"]
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filename)
        return redirect(url_for("index"))
    return "Invalid file type"


if __name__ == "__main__":
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])
    app.run(debug=True)
