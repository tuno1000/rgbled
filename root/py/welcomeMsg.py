import sys
import subprocess
import time
import RPi.GPIO as GPIO

args = sys.argv

INTERVAL = 3
SLEEPTIME = 10
GPIO_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

try:
    while True:
        if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
            subprocess.run(["sh /data/nodejs/viewTextAT.sh " + args[1] + "______ " + args[2]],shell=True)
            time.sleep(SLEEPTIME)
        else:
            time.sleep(INTERVAL)
finally:
    GPIO.cleanup()
