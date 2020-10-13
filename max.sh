#!/bin/sh
echo "Program to find the max value of n numbers."
read -p "Enter n: " n
read -p "Enter number: " max
while [ $n -gt 1 ]
do
    read -p "Enter number: " i
    if [ $i -gt $max ]
    then
        max=$i 
    fi 
    n=$(($n-1))
done
echo "The largest number is $max"
read -p "Press Enter to continue..." n
