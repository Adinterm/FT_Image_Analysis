from pytesseract import image_to_string
import pytesseract
import PIL.Image
import glob
import cv2
import os

os.chdir() #choose the directory here
format_file = 'JPG'
files = sorted(glob.glob('*.{}'.format(format_file)
               
#Linux
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
#for windows user, try to find the file inside the program files directory

#the position of the text you want to get (in pixel)
y = #value
x = #value
height = #value
width = #value

for i in range(0,len(files)):
  image = cv2.imread(files[i])
  crop_img = image[y:y+height, x:x+width]
  output = pytesseract.image_to_string(crop, lang='eng')
  os.rename(files[i], "{}.{}".format(output, format_file))
               
print(files)
