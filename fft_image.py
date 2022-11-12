import matplotlib.pyplot as plt
import numpy as np

def fft.img(imgpath):
  imr = plt.imread(imgpath)
  fft_img = np.fft.fftshift(np.fft.fft2(rgb2gray(imr)))
  return fft_img

def get_peak(array):
  imgarray = array
  ir_1 = imgarray[0]
  for i in range(0,len(imgarray)):
    if ir_1 < imgarray[i]:
      ir_1 =imgarray[i]
      
  
