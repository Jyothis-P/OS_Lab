#!/bin/sh
echo "Program to find the sum of n numbers."
read -p "Enter n: " n
i=1
sum=0
while [ $i -le $n ]
do 
	read -p "Enter number $i: " num
	sum=$(($sum+num))
	i=$(($i+1))
done
echo $sum
read -p "Press Enter to continue..." n
