import logging
from flask import Flask, request
import image_detection

app = Flask(__name__)

@app.route('/image_detect', methods=['GET', 'POST'])
def handle():
    input = request.get_json()
    photo_link = input.get('photo_link')
    if photo_link is None:
        return "No photo found", 400

    return image_detection.run(photo_link=photo_link, detection_type="face")
