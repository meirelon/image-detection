import argparse
from downloadImage import download_image

def run_quickstart(photo_link):
    # [START vision_quickstart]
    import io
    import os

    # Imports the Google Cloud client library
    # [START vision_python_migration_import]
    from google.cloud import vision
    from google.cloud.vision import types
    # [END vision_python_migration_import]

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

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)
    # [END vision_quickstart]


def main(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument('--photo-link',
                        dest='photo_link',
                        default = None,
                        help='Link to a photo')

    args, _ = parser.parse_known_args(argv)

    run_quickstart(photo_link=args.photo_link)

if __name__ == '__main__':
    main()
