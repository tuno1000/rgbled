#!/bin/bash

contents=$(/usr/bin/curl -s $1)

#echo ${contents}

content=$(echo ${contents} | grep "meta name=\"description\" content=\"")

#echo ${content} | wc -l

s=$(echo ${content} | awk '{print index($0, "meta name=\"description\" content=\"")}')

eee=$(echo ${content} | cut -b $((s+33))-)

e=$(echo ${eee} | awk '{print index($0, "\"")}')

echo $(echo ${eee} | cut -b 1-$((e-1)))

exit 0
