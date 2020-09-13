#!/bin/bash

news=$(/usr/bin/curl https://news.yahoo.co.jp/pickup/domestic/rss.xml | grep -e title -e link)

work=$(echo ${news} | sed -E 's/ /_/g')
work=$(echo ${work} | sed -E 's/<title>//g')
work=$(echo ${work} | sed -E 's/<\/title>/ /g')
work=$(echo ${work} | sed -E 's/<link>//g')
work=$(echo ${work} | sed -E 's/<\/link>/ /g')

array=(${work})

n=1
for i in "${array[@]}"
do
	i=$(echo ${i} | sed -E 's/^_//g')
	echo ${i}
	echo ${n}

	if [ `expr $n % 2` == 0 ]; then
  		echo ${array[$((n-2))]}
                echo ${i}
		echo $(/data/nodejs/newsDetail.sh ${i})
		#str="\"${array[$((n-2))]} $(/data/nodejs/newsDetail.sh ${i})\""
		str="${array[$((n-2))]}_$(/data/nodejs/newsDetail.sh ${i})"
                #echo ${str}
		$(sh /data/nodejs/viewTextAT.sh ${str} 255,255,255)
		echo $(/usr/bin/python /data/nodejs/getViewTime.py)
	fi

	n=$((n+1))
done
