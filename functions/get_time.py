from PIL import Image
from PIL.ExifTags import TAGS

def get_time(img):
    image = Image.open(img)
    return Image.open(img)._getexif()[36867] #36867 is for time metadata, see the documentation
