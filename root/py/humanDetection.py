import subprocess
import time
import RPi.GPIO as GPIO

INTERVAL = 3
SLEEPTIME = 20
GPIO_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

try:
    while True:
        if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
            subprocess.run(["/root/rpi-rgb-led-matrix/examples-api-use/demo --led-no-hardware-pulse --led-rows=16 --led-cols=32 -D 1 -c 2 -t 10 /var/tmp/emergency.ppm"],shell=True)
            time.sleep(SLEEPTIME)
        else:
            time.sleep(INTERVAL)
finally:
    GPIO.cleanup()
