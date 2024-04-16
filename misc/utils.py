import io
from PIL import Image

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'jfif'}


def convert_to_binary(img):
    image = Image.open(img)
    byte_stream = io.BytesIO()
    image.save(byte_stream, format=F'PNG')
    byte_image = byte_stream.getvalue()
    return byte_image


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS