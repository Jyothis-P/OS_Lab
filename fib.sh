#! /bin/sh
read -p "enter n" n
first=0
second=1
echo $first
echo $second
i=3
while [ $i -le $n ]
do
	third=$(($first+$second))
	echo $third
	first=$second
	second=$third
	i=$(($i+1))
done
