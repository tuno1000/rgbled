#encoding:UTF-8
#-*- codinf:utf-8 -*-
from PIL import Image

img = Image.open("/var/tmp/em.ppm")
width, height = img.size

print(round(width / 45.0) )

img = img.resize((int(img.width / (img.height / 16 )), 16))
img.save("/var/tmp/resize.ppm")
