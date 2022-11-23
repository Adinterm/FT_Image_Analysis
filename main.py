import math
import os, glob
from PIL import Image
from PIL.ExifTags import TAGS
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import numpy as np

#change directory
os.chdir('/content/drive/MyDrive/TA_HSV/Images2')

#create list of files
files = sorted(glob.glob('*.JPG'))

#fft image
def fft_img(imgpath):
  imr = plt.imread(imgpath)
  fft_img = np.fft.fftshift(np.fft.fft2(rgb2gray(imr)))
  return np.array(fft_img)

#highest value from an array
def get_peak(array):
  peak_ar = np.array(array)
  axis = peak_ar.shape[1]
  axis2 = int(axis/2)
  axisy = peak_ar[:,axis2]
  ir_1 = [0]
  for i in range(0,len(axisy)):
    if ir_1 < axisy[i]:
      ir_1 = axisy[i]
  return ir_1

#get time from image metadata
def get_time(img):
    image = Image.open(img)
    return Image.open(img)._getexif()[36867] #36867 is for time metadata, see the documentation

def sunpos(when, location, refraction):
  # Extract the passed data
  year, month, day, hour, minute, second, timezone = when
  latitude, longitude = location

  # Math typing shortcuts
  rad, deg = math.radians, math.degrees
  sin, cos, tan = math.sin, math.cos, math.tan
  asin, atan2 = math.asin, math.atan2

  # Convert latitude and longitude to radians
  rlat = rad(latitude)
  rlon = rad(longitude)
    
  # Decimal hour of the day at Greenwich
  greenwichtime = hour - timezone + minute / 60 + second / 3600# Days from J2000, accurate from 1901 to 2099
  daynum = (
      367 * year
      - 7 * (year + (month + 9) // 12) // 4
      + 275 * month // 9
      + day
      - 730531.5
      + greenwichtime / 24
    )
  # Mean longitude of the sun
  mean_long = daynum * 0.01720279239 + 4.894967873

  # Mean anomaly of the Sun
  mean_anom = daynum * 0.01720197034 + 6.240040768

  # Ecliptic longitude of the sun
  eclip_long = (
      mean_long
      + 0.03342305518 * sin(mean_anom)
      + 0.0003490658504 * sin(2 * mean_anom)
      )
  # Obliquity of the ecliptic
  obliquity = 0.4090877234 - 0.000000006981317008 * daynum

  # Right ascension of the sun
  rasc = atan2(cos(obliquity) * sin(eclip_long), cos(eclip_long))

  # Declination of the sun
  decl = asin(sin(obliquity) * sin(eclip_long))

  # Local sidereal time
  sidereal = 4.894961213 + 6.300388099 * daynum + rlon

  # Hour angle of the sun
  hour_ang = sidereal - rasc# Local elevation of the sun
  elevation = asin(sin(decl) * sin(rlat) + cos(decl) * cos(rlat) * cos(hour_ang))

  # Local azimuth of the sun
  azimuth = atan2(
      -cos(decl) * cos(rlat) * sin(hour_ang),
      sin(decl) - sin(rlat) * sin(elevation),
      )
  
  # Convert azimuth and elevation to degrees
  azimuth = into_range(deg(azimuth), 0, 360)
  elevation = into_range(deg(elevation), -180, 180)

  # Refraction correction (optional)
  if refraction:
    targ = rad((elevation + (10.3 / (elevation + 5.11))))
    elevation += (1.02 / tan(targ)) / 60

  # Return azimuth and elevation in degrees
  return (round(azimuth, 2), round(elevation, 2))

def into_range(x, range_min, range_max):
  shiftedx = x - range_min
  delta = range_max - range_min
  return (((shiftedx % delta) + delta) % delta) + range_min

def center_rc(img,rc):    #use (image array, [0 = row, 1 = column])
  peak_ar = np.array(img)
  edge = peak.shape[rc]
  edge2 = edge/2
  if rc == 0:
    peak_rc = peak_ar[edge2,:]
  if rc == 1:
    peak_rc = peak_ar[:,edge2]
  ir_1 = [0]
  for i in range(0,len(peak_rc)):
    if ir_1 < peak_rc[i]
      ir_1 = peak_rc[i]
    return ir_1

def get_peak_rc(img,rc):    #use (image array, [0 = row, 1 = column])
  peak_ar = np.array(img)
  edge = rc
  if rc == 0:
    peak_rc = peak_ar[edge2,:]
  if rc == 1:
    peak_rc = peak_ar[:,edge2]
  ir_1 = [0]
  for i in range(0,len(peak_rc)):
    if ir_1 < peak_rc[i]
      ir_1 = peak_rc[i]
    return ir_1

def get_peak_rc(img, rc, rc2):
  peak_ar = np.array(img)
  if rc == 0:
    peak_rc = peak_ar[rc2,:]
  if rc == 1:
    peak_rc = peak_ar[:,rc2]
  ir_1 = [0]
  for i in range(0, len(peak_rc)):
    if ir_1 < peak_rc[i]
      ir_1 = peak_rc[i]
    return ir_1

def get_peak_rc(img):
  for i in range(0, len(img.shape[0])):
    get_row = peak_rc(img,0,i)
  print("Length row = {}".format(len(img.shape[0])))
  
  for i in range(0, len(img.shape[1])):
    get_column = peak_rc(img,1,i)
  print("Length column = {}".format(len(img.shape[1])))
  return get_row, get_column
    
  
  
##############################################################

if __name__ == "__main__":
  location = (-6.832327, 107.618571)
  time_zone = [7]
  date = [2018, 4, 24]
  ar_peak = []
  elvt = []
  c = []

  for i in range(0,len(files)):
    fft_image = fft_img(files[i])
    peak = get_peak(fft_image)
    ar_peak = ar_peak+[peak]
    #time
    gt_time = get_time(files[i])
    gt_time = gt_time[11:19]
    gt_time = gt_time.split(":")
    tm = [int(x) for x in gt_time]
    tm_lst = date + tm + time_zone
    when = tuple(tm_lst)
    #elevation
    sunp = sunpos(when, location, True)
    elvt = elvt + [sunp[1]]

