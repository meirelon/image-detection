import os
import urllib.request

import requests
from google.appengine.api import images
# import cloudstorage as gcs

# from PIL import Image

# def read_image_from_url(photo_link):
#     r = requests.get(photo_link)
#     return Image.open(BytesIO(r.content))


def download_image(photo_link):
    file_path = os.path.join(os.path.dirname(__file__),"resources/pics/photo.jpg")
    urllib.request.urlretrieve(photo_link, file_path)

def read_image_from_url(url):
    image_at_url = requests.get(url)
    content_type =  image_at_url.headers['Content-Type']
    filename = "path/to/gcs/file"

    image_bytes = image_at_url.read()
    image_at_url.close()
    image = images.Image(image_bytes)

    # this comes in handy if you want to resize images:
    if image.width > 800 or image.height > 800:
        image = images.resize(image_bytes, 800, 800)
    return image
