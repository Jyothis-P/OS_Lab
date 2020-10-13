#!/bin/sh
echo "Program to output the reverse of a string."
read -p "Enter the string: " st
len= ${#st}
echo "Length of the string is $len"
rev=""
for ((i = 0; i < $len; i++))
do
    rev=$rev${st:$((len - i - 1)):1}
    # echo "${st:$((len - i - 1)):1}"
done
echo
echo "Original String: $st"
echo "Reverse: $rev"
if [ $st == $rev ]
then
    echo "String is a Pallindrome."
fi
read -p "Press Enter key to continue..." n
