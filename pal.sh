#! /bin/sh
read -p "Enter the string" str
re=$(echo $str | rev )
if [ $str = $re ]
then
	echo " String is a palindrome"
else
	echo "string is not a palindrome "
fi