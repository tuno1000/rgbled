#!bin/bash

kill `ps -ax | grep viewYahooNews.sh | awk '{print $1}'`
#kill `pidof /bin/sh /data/nodejs/viewYahooNews.sh | awk '{print $1}'`

exit 0

