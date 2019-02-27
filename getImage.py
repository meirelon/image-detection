import os
import urllib.request

from PIL import Image
import requests
from io import BytesIO

def download_image(photo_link):
    file_path = os.path.join(os.path.dirname(__file__),"resources/pics/photo.jpg")
    urllib.request.urlretrieve(photo_link, file_path)

def read_image_from_url(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))

    # this comes in handy if you want to resize images:
    if image.width > 800 or image.height > 800:
        image.resize(800, 800)
    return image
