from PIL import Image
from PIL.ExifTags import TAGS


imagename = files
image = Image.open(imagename)
def get_date_taken(path):
    return Image.open(path)._getexif()[36867] #36867 is for time metadata, see the documentation
print(get_date_taken(imagename))
a = get_date_taken(imagename)

print(type(a))
print(a[11:])
