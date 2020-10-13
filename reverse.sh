#!/bin/sh
echo "1. Write a script to check whether a given string is a palindrome."
read -p "Enter the string: " st
len=${#st}
echo
echo "Length of the string is $len"
rev=""
for ((i = 0; i < len; i++)); do
  rev=$rev${st:$((len - i - 1)):1}
  # echo "${st:$((len - i - 1)):1}"
done
echo
echo "Original String: $st"
echo "Reverse: $rev"
echo
if [ $st == $rev ]; then
  echo "String is a Palindrome."
else
  echo "String is not a Palindrome"
fi
echo
read -p "Press Enter key to continue..." n
