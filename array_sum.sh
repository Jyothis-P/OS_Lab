#!/bin/sh
echo "Program to find the sum of an array."
read -p "Enter the number of elements in the array: " n 
i=0
while [ $i -lt $n ]
do 
    read -p "Enter element number $i: " arr[$i]
    i=$((i+1))
done

echo "Array: ${arr[*]}"
sum=0
for (( i=0; i < $n; i++ ))
do
    sum=$((sum+${arr[$i]}))
    # echo ${arr[*]}
done
echo Sum: $sum
read -p "Press Enter key to continue..." n