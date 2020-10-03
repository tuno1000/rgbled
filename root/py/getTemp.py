import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

def get_temp():

	# read data using pin 14
	instance = dht11.DHT11(pin=21)

	try:
		temp = []
		result = instance.read()
		while True:
			if result.is_valid():
				temp = result.temperature
			if temp:
				break
			result = instance.read()
			time.sleep(1)

		temp = result.temperature
		n = "%02d" % temp
		s = str(temp).split('.')[1][0]

	except:
		GPIO.cleanup()

	return [n[0],n[1],s[0]]

get_temp()
