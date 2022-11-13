import matplotlib.pyplot as plt
import numpy as np

def fft.img(imgpath):
  imr = plt.imread(imgpath)
  fft_img = np.fft.fftshift(np.fft.fft2(rgb2gray(imr)))
  return fft_img

def get_peak(array):
  imgarray = np.array(array)
  axis = imgarray.shape[1]
  axis = axis/2
  ir_1 = axis
  for i in range(0,len(imgarray)):
    if ir_1 < imgarray[i]:
      ir_1 = imgarray[i]
  return ir_1
      
  
