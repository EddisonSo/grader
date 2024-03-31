from flask import Flask
from api.file_service import upload_service

if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(upload_service)
    app.run(host="0.0.0.0", port=5050)
