

from flask import Flask, render_template, request, redirect

import os

app = Flask(__name__)
@app.route("/file-upload-view", methods=["GET"])
def load_fileupload_page():
    return render_template("file_upload.html")

@app.route("/file-upload", methods=["POST"])
def handle_fileupload():
    files = request.files
    file = files['file-to-send']
    save_files(file)
    file = files['file-to-send2']
    save_files(file)
    file = files['file-to-send3']
    save_files(file)

    return redirect("/file-upload-view")


def save_files(file):
    if file:
        file.save(os.path.join("uploads", file.filename))


if __name__ == "__main__":
    app.run(debug=True)