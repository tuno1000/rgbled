import RPi.GPIO as GPIO
import time
import random

delay = 0.000001

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

led_x = 64
led_y = 16

red1_pin = 11
green1_pin = 27
blue1_pin = 7
red2_pin = 8
green2_pin = 9
blue2_pin = 10
clock_pin = 17
a_pin = 22
b_pin = 23
c_pin = 24
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

#set_pixel(0,0,4)
#set_pixel(31,15,1)
#set_pixel(32,0,4)
#set_pixel(63,15,1)

while True:
    set_init()
    refresh()
    for x in range(led_x):
        c = random.randrange(1,8)
        for y in range(led_y):
            set_pixel(x,y,c)
            refresh()
