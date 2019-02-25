import argparse
from downloadImage import download_image

def run_quickstart(photo_link, detection_type="label", from_internet=True):
    # [START vision_quickstart]
    import io
    import os

    # Imports the Google Cloud client library
    # [START vision_python_migration_import]
    from google.cloud import vision
    from google.cloud.vision import types
    # [END vision_python_migration_import]
    if from_internet:
        download_image(photo_link)

    # Instantiates a client
    # [START vision_python_migration_client]
    client = vision.ImageAnnotatorClient()
    # [END vision_python_migration_client]

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        'resources/pics/photo.jpg')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    if detection_type=="label":
        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        print('Labels:')
        for label in labels:
            print(label.description)

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

def main(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument('--photo-link',
                        dest='photo_link',
                        default = None,
                        help='Link to a photo')

    parser.add_argument('--detection-type',
                        dest='detection_type',
                        default = None,
                        help='Label or Text Detection')

    args, _ = parser.parse_known_args(argv)

    run_quickstart(photo_link=args.photo_link, detection_type=args.detection_type)

if __name__ == '__main__':
    main()
