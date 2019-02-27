import os
import urllib.request

def download_image(photo_link):
    file_path = os.path.join(os.path.dirname(__file__),"resources/pics/photo.jpg")
    urllib.request.urlretrieve(photo_link, file_path)
