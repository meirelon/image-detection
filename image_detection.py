import argparse #convert this to docker env variables
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

#From download image utility
from getImage import download_image

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

def run(photo_link, detection_type="face", from_internet=True):

    if from_internet:
        download_image(photo_link)

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        'resources/pics/photo.jpg')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        photo = image_file.read()

    image = types.Image(content=photo)

    if detection_type=="label":
        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        print('Labels:')
        label_list = [label.description for label in labels]
        return " ".join(label_list)

    elif detection_type == "text":
        response = client.text_detection(image=image)
        words = []
        for page in response.full_text_annotation.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        word_text = ''.join([
                            symbol.text for symbol in word.symbols
                        ])
                        words.append(word_text.lower())
        return " ".join(words)

    elif detection_type == "face":
        response = client.face_detection(image=image)
        face = response.face_annotations[0]
        emotion_dictionary = {"happy":face.joy_likelihood,
                             "sad":face.sorrow_likelihood,
                             "anger":face.anger_likelihood,
                             "surprised":face.surprise_likelihood}
        emotion_list = []
        for k,v in emotion_dictionary.items():
            if v == 5:
                emotion_list.append(k)
        if len(emotion_list) > 0:
            print(emotion_list[0])
            return emotion_list[0]
        else:
            return 'neutral'


def main(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument('--photo-link',
                        dest='photo_link',
                        default = None,
                        help='Link to a photo')

    parser.add_argument('--detection-type',
                        dest='detection_type',
                        default = 'label',
                        help='Label or Text Detection')

    args, _ = parser.parse_known_args(argv)

    run(photo_link=args.photo_link, detection_type=args.detection_type)

if __name__ == '__main__':
    main()
