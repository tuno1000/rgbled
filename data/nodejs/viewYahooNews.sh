#!/bin/bash

rgb=$1

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
	if [ ${n} = 1 -o ${n} = 2 ]; then
		n=$((n+1))
		continue
	fi

	i=$(echo ${i} | sed -E 's/^_//g')
	#echo ${i}
	#echo ${n}

	if [ `expr $n % 2` == 0 ]; then
  		#echo ${array[$((n-2))]}
                #echo ${i}
		#echo $(/data/nodejs/newsDetail.sh ${i})
		#str="\"${array[$((n-2))]} $(/data/nodejs/newsDetail.sh ${i})\""
		str="${array[$((n-2))]}_$(/data/nodejs/newsDetail.sh ${i})____"
                #echo ${str}
		$(sh /data/nodejs/viewTextAT.sh ${str} ${rgb})
		#echo $(/usr/bin/python /data/nodejs/getViewTime.py)
	fi

	n=$((n+1))
done
