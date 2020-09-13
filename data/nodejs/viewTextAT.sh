#!/bin/bash

rgbpath="/root/rpi-rgb-led-matrix/examples-api-use/"

/usr/bin/python /data/nodejs/makePpm.py $1 $2

timeLen=$(/usr/bin/python /data/nodejs/getViewTime.py)

${rgbpath}demo --led-no-hardware-pulse --led-rows=16 --led-cols=32 -D 1 -m 20 -c 2 -t ${timeLen} /var/tmp/text.ppm

exit 0
