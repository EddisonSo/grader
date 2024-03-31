from flask import Flask, request, Blueprint
from werkzeug.utils import secure_filename
from api.config import *

upload_service = Blueprint("upload_service", __name__, template_folder="templates")

@upload_service.route("/get", methods=["POST", "GET"])
def get():
    return ('', 204)

@upload_service.route("/upload", methods=["POST"])
def upload():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file.save(join(UPLOADS_PATH, filename))
        return "success"
    return "failed"
