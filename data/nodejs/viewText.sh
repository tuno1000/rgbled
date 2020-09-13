#!/bin/bash

rgbpath="/root/rpi-rgb-led-matrix/examples-api-use/"

/usr/bin/python /data/nodejs/makePpm.py $1 $3

${rgbpath}demo --led-no-hardware-pulse --led-rows=16 --led-cols=32 -D 1 -m 20 -c 2 /var/tmp/text.ppm -t $2

exit 0
