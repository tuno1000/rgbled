import RPi.GPIO as GPIO
import time
import random
import getTemp
import getTime

delay = 0.000001

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

led_x = 64; led_y = 16

red1_pin = 11; green1_pin = 27; blue1_pin = 7
red2_pin = 8; green2_pin = 9; blue2_pin = 10
clock_pin = 17
a_pin = 22; b_pin = 23; c_pin = 24
latch_pin = 4
oe_pin = 18

GPIO.setup(red1_pin, GPIO.OUT)
GPIO.setup(green1_pin, GPIO.OUT)
GPIO.setup(blue1_pin, GPIO.OUT)
GPIO.setup(red2_pin, GPIO.OUT)
GPIO.setup(green2_pin, GPIO.OUT)
GPIO.setup(blue2_pin, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(a_pin, GPIO.OUT)
GPIO.setup(b_pin, GPIO.OUT)
GPIO.setup(c_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT)
GPIO.setup(oe_pin, GPIO.OUT)

screen = [[0 for x in range(led_x)] for x in range(led_y)]

def clock():
    GPIO.output(clock_pin, 1)
    GPIO.output(clock_pin, 0)

def latch():
    GPIO.output(latch_pin, 1)
    GPIO.output(latch_pin, 0)

def bits_from_int(x):
    a_bit = x & 1
    b_bit = x & 2
    c_bit = x & 4
    return (a_bit, b_bit, c_bit)

def set_row(row):
    #time.sleep(delay)
    #print("row:",row)
    a_bit, b_bit, c_bit = bits_from_int(row)
    #print(a_bit, b_bit, c_bit)
    GPIO.output(a_pin, a_bit)
    GPIO.output(b_pin, b_bit)
    GPIO.output(c_pin, c_bit)
    #time.sleep(delay)

def set_color_top(color):
    #time.sleep(delay)
    red, green, blue = bits_from_int(color)
    GPIO.output(red1_pin, red)
    GPIO.output(green1_pin, green)
    GPIO.output(blue1_pin, blue)
    #time.sleep(delay)

def set_color_bottom(color):
    #time.sleep(delay)
    red, green, blue = bits_from_int(color)
    GPIO.output(red2_pin, red)
    GPIO.output(green2_pin, green)
    GPIO.output(blue2_pin, blue)
    #time.sleep(delay)

def refresh():
    for row in range(8):
        GPIO.output(oe_pin, 1)
        #set_color_top(0)
        #set_row(row)
        #time.sleep(delay)

        for col in range(led_x):
            set_color_top(screen[row][col])
            set_color_bottom(screen[row+8][col])
            clock()
            #GPIO.output(oe_pin, 0)
        set_row(row)
        latch()
        GPIO.output(oe_pin, 0)
        time.sleep(delay)

def fill_rectangle(x1, y1, x2, y2, color):
    for x in range(x1, x2):
        for y in range(y1, y2):
            screen[y][x] = color

def set_pixel(x, y, color):
    screen[y][x] = color

def set_init():
    for x in range(led_x):
        for y in range(led_y):
            screen[y][x] = 0

#fill_rectangle(0, 2, 10, 14, 1)
#fill_rectangle(15, 0, 19, 7, 4)
#fill_rectangle(20, 4, 30, 14, 2)

def set_num(n,x,y,coler):
    if n == 1:
        set_pixel(0+x,2+y,coler)
        set_pixel(1+x,1+y,coler)
        set_pixel(2+x,0+y,coler);set_pixel(2+x,1+y,coler);set_pixel(2+x,2+y,coler)
        set_pixel(2+x,3+y,coler);set_pixel(2+x,4+y,coler);set_pixel(2+x,5+y,coler)
    elif n == 2:
        set_pixel(0+x,1+y,coler);set_pixel(0+x,4+y,coler);set_pixel(0+x,5+y,coler)
        set_pixel(1+x,0+y,coler);set_pixel(1+x,3+y,coler);set_pixel(1+x,5+y,coler)
        set_pixel(2+x,0+y,coler);set_pixel(2+x,3+y,coler);set_pixel(2+x,5+y,coler)
        set_pixel(3+x,1+y,coler);set_pixel(3+x,2+y,coler);set_pixel(3+x,5+y,coler)
    elif n == 3:
        set_pixel(0+x,1+y,coler);set_pixel(0+x,4+y,coler);
        set_pixel(1+x,0+y,coler);set_pixel(1+x,5+y,coler);
        set_pixel(2+x,0+y,coler);set_pixel(2+x,2+y,coler);set_pixel(2+x,5+y,coler);
        set_pixel(3+x,1+y,coler);set_pixel(3+x,3+y,coler);set_pixel(3+x,4+y,coler);
    elif n == 4:
        set_pixel(0+x,2+y,coler);set_pixel(0+x,3+y,coler);
        set_pixel(1+x,1+y,coler);set_pixel(1+x,3+y,coler);
        set_pixel(2+x,0+y,coler);set_pixel(2+x,3+y,coler);
        set_pixel(3+x,0+y,coler);set_pixel(3+x,1+y,coler);set_pixel(3+x,2+y,coler);
        set_pixel(3+x,3+y,coler);set_pixel(3+x,4+y,coler);set_pixel(3+x,5+y,coler);
    elif n == 5:
        set_pixel(0+x,0+y,coler);set_pixel(0+x,1+y,coler);set_pixel(0+x,2+y,coler);set_pixel(0+x,4+y,coler);
        set_pixel(1+x,0+y,coler);set_pixel(1+x,2+y,coler);set_pixel(1+x,5+y,coler);
        set_pixel(2+x,0+y,coler);set_pixel(2+x,2+y,coler);set_pixel(2+x,5+y,coler);
        set_pixel(3+x,0+y,coler);set_pixel(3+x,3+y,coler);set_pixel(3+x,4+y,coler);
    elif n == 6:
        set_pixel(0+x,1+y,coler);set_pixel(0+x,2+y,coler);set_pixel(0+x,3+y,coler);set_pixel(0+x,4+y,coler);
        set_pixel(1+x,0+y,coler);set_pixel(1+x,3+y,coler);set_pixel(1+x,5+y,coler);
        set_pixel(2+x,0+y,coler);set_pixel(2+x,3+y,coler);set_pixel(2+x,5+y,coler);
        set_pixel(3+x,1+y,coler);set_pixel(3+x,4+y,coler);
    elif n == 7:
        set_pixel(0+x,0+y,coler);set_pixel(1+x,4+y,coler);set_pixel(1+x,5+y,coler);
        set_pixel(1+x,0+y,coler);set_pixel(1+x,3+y,coler);
        set_pixel(2+x,0+y,coler);set_pixel(2+x,2+y,coler);
        set_pixel(3+x,0+y,coler);set_pixel(3+x,1+y,coler);
    elif n == 8:
        set_pixel(0+x,1+y,coler);set_pixel(0+x,3+y,coler);set_pixel(0+x,4+y,coler);
        set_pixel(1+x,0+y,coler);set_pixel(1+x,2+y,coler);set_pixel(1+x,5+y,coler);
        set_pixel(2+x,0+y,coler);set_pixel(2+x,2+y,coler);set_pixel(2+x,5+y,coler);
        set_pixel(3+x,1+y,coler);set_pixel(3+x,3+y,coler);set_pixel(3+x,4+y,coler);
    elif n == 9:
        set_pixel(0+x,1+y,coler);set_pixel(0+x,4+y,coler);
        set_pixel(1+x,0+y,coler);set_pixel(1+x,2+y,coler);set_pixel(1+x,5+y,coler);
        set_pixel(2+x,0+y,coler);set_pixel(2+x,2+y,coler);set_pixel(2+x,5+y,coler);
        set_pixel(3+x,1+y,coler);set_pixel(3+x,2+y,coler);set_pixel(3+x,3+y,coler);set_pixel(3+x,4+y,coler);
    elif n == 0:
        set_pixel(0+x,1+y,coler);set_pixel(0+x,2+y,coler);set_pixel(0+x,3+y,coler);set_pixel(0+x,4+y,coler);
        set_pixel(1+x,0+y,coler);set_pixel(1+x,5+y,coler);
        set_pixel(2+x,0+y,coler);set_pixel(2+x,5+y,coler);
        set_pixel(3+x,1+y,coler);set_pixel(3+x,2+y,coler);set_pixel(3+x,3+y,coler);set_pixel(3+x,4+y,coler);
    elif n == 99:
        set_pixel(0+x,5+y,coler);

#set_num(0,0,0,1)
#set_num(1,5,0,1)
#set_num(2,10,0,1)
#set_num(3,15,0,1)
#set_num(4,20,0,1)
#set_num(5,25,0,1)
#set_num(6,30,0,1)
#set_num(7,35,0,1)
#set_num(8,40,0,1)
#set_num(9,45,0,1)

ccoler = 3
t = getTime.get_timeArry()
set_num(int(t[0]),33,1,ccoler)
set_num(int(t[1]),38,1,ccoler)
set_pixel(43,2,ccoler)
set_pixel(43,5,ccoler)
set_num(int(t[2]),45,1,ccoler)
set_num(int(t[3]),50,1,ccoler)

tcoler = 2
temp = getTemp.get_temp()
set_num(int(temp[0]),1,1,tcoler)
set_num(int(temp[1]),6,1,tcoler)
set_num(99,11,1,tcoler)
set_num(int(temp[2]),12,1,tcoler)

hcoler = 4
set_num(int(temp[3]),1,9,hcoler)
set_num(int(temp[4]),6,9,hcoler)
set_num(99,11,9,hcoler)
set_num(int(temp[5]),12,9,hcoler)

while True:

    if time.localtime()[5] % 61 == 0:
        temp = getTemp.get_temp()
        set_init()
        set_num(int(temp[0]),1,1,tcoler)
        set_num(int(temp[1]),6,1,tcoler)
        set_num(99,11,1,tcoler)
        set_num(int(temp[2]),12,1,tcoler)
        
        set_num(int(temp[3]),1,9,hcoler)
        set_num(int(temp[4]),6,9,hcoler)
        set_num(99,11,9,hcoler)
        set_num(int(temp[5]),12,9,hcoler)
    
        t = getTime.get_timeArry()
        set_num(int(t[0]),33,1,ccoler)
        set_num(int(t[1]),38,1,ccoler)
        set_pixel(43,2,ccoler)
        set_pixel(43,5,ccoler)
        set_num(int(t[2]),45,1,ccoler)
        set_num(int(t[3]),50,1,ccoler)

    refresh()

