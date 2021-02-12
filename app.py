from flask import Flask
import tensorflow as tf
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/hello")
def index():
    return {'result': "Hello world"}
