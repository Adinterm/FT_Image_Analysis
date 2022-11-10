from pytesseract import image_to_string
import pytesseract
import PIL.Image
import cv2

#Linux
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
#for windows user, try to find the file inside the program files directory

'''<input_image> add later'''

image = cv2.imread(input_image)
y = #value
x = #value
height = #value
width = #value

crop_img = image[y:y+h, x:x+w]

output = pytesseract.image_to_string(crop, lang='eng')
print(output)
