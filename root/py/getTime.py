import time

def get_timeArry():

	h = "%02d" % time.localtime()[3]
	m = "%02d" % time.localtime()[4]
	return [h[0],h[1],m[0],m[1]]

