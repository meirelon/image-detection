import os
import urllib.request

# from PIL import Image
import requests
from io import BytesIO

def read_image_from_url(photo_link):
    r = requests.get(url)
    return BytesIO(r.content)


def download_image(photo_link):
    file_path = os.path.join(os.path.dirname(__file__),"resources/pics/photo.jpg")
    urllib.request.urlretrieve(photo_link, file_path)
