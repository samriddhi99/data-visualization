
from flask import Flask, json, request, jsonify
from data_summarization.summarised_txt import get_summarised_txt
import os
import urllib.request
from werkzeug.utils import secure_filename

from summarization.input_processing import *
from summarization.summarised_txt import *
from summarization.data_processing import *


import pandas as pd
import numpy as np


app = Flask(__name__)

app.secret_key = "caircocoders-ednalan"

UPLOAD_FOLDER = "Users/monishakollipara/Desktop/flaskfiles"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif", "csv"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def main():
    return "Homepage"


@app.route("/upload", methods=["POST"])
def upload_file():
    # check if the post request has the file part
    if "file" not in request.files:
        resp = jsonify({"message": "No file part in the request"})
        resp.status_code = 400
        return resp

    files = request.files.getlist("file")

    errors = {}
    success = False

    for file in files:
        if file and allowed_file(file.filename):
            df = pd_dataframe(file)
            op = get_summarised_txt(df)
            resp = jsonify({"summary" : op})
            resp.status_code = 201
            return resp
        else:
            errors[file.filename] = "File type is not allowed"

    if success and errors:
        errors["message"] = "File(s) successfully uploaded"
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        resp = jsonify({"message": "Files successfully uploaded"})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp


if __name__ == "__main__":
    app.run(debug=True)