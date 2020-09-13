#encoding:UTF-8
#-*- codinf:utf-8 -*-
from PIL import Image

img = Image.open("/var/tmp/text.ppm")
width, height = img.size

print(round(width / 44.0) )

