#encoding:UTF-8
#-*- codinf:utf-8 -*-
import sys
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

args = sys.argv
#print(args[1])
inText = args[1].decode('utf-8')

rgb = args[2].split(",")
list = list(map(int,rgb))
#print(list)

viewText = []

viewText.append( ((u"    ") + inText ,tuple(list)))

text = tuple(viewText)

font = ImageFont.truetype("/usr/share/fonts/truetype/takao-mincho/TakaoMincho.ttf", 16)
all_text = ""
for text_color_pair in text:
    t = text_color_pair[0]
    all_text = all_text + t
 
#print(all_text)
width, ignore = font.getsize(all_text)
#print(width)
 
 
im = Image.new("RGB", (width + 30, 16), "black")
draw = ImageDraw.Draw(im)
 
x = 0;
for text_color_pair in text:
    t = text_color_pair[0]
    c = text_color_pair[1]
    #print("t=" + t + " " + str(c) + " " + str(x))
    draw.text((x, 0), t, c, font=font)
    x = x + font.getsize(t)[0]
 
im.save("/var/tmp/text.ppm")
