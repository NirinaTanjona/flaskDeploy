import os
import tensorflow as tf
import numpy as np
import PIL
import matplotlib.pyplot as plt
from flask_cors import CORS
from flask import Flask, request, session, jsonify
from PIL import Image
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/tanjona/Documents/flask-api'
ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

# import the keras model
# loaded_model = tf.keras.models.load_model('keras.h5')


@app.route("/predict", methods=["POST", "GET"])
def predict():
    # TODO: get take the image via POST
    target = os.path.join(UPLOAD_FOLDER, 'test_docs')
    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination = "/".join([target, filename])
    file.save(destination)
    response = "Done"

    # TODO: preprocessing DATA and predict
    image = tf.keras.preprocessing.image.load_img(destination)
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    # TODO: return the prediction in form of JSON using jasonify

    return jsonify(response)


if __name__ == '__main__':
    predict()
