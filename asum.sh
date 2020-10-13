#! /bin/bash
read -p "Enter n :" n
i=0
while [ $i -lt $n ]
do
	read -p "Enter the number" num
	arr+=( $num )
	i=$(($i+1))
	
done
for j in ${arr[*]}
do
	sum=$(($sum+j))
done
echo $sum
