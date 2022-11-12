import os, glob
import take_time

files = sorted(glob.glob('*.JPG'))

for a in range(0,len(files)):
  t = take_time.get_time(files[a])
  print(t[11:])
