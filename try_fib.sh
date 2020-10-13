#! /bin/sh
echo "Program to print the first n numbers in the Fibonacci Series."
read -p "Enter n: " n
a=0
b=1
res=$a
echo $a
while [ $n -gt 1 ]
do
    res=$res" "$b
    echo $b
    t=$b
    b=$(($a+$b))
    a=$t
    n=$(($n-1))
done
echo "Fibonacci: $res"
read -p "Press Enter key to continue..." n
