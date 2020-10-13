import os
import sys

r, w = os.pipe()
process_id = os.fork()
if (process_id > 0):
    n = str(input("enter the numbers"))
    os.close(r)
    os.write(w, n.encode())
else:
    a = ""
    n = os.read(r, 200)
    n = n.decode()
    print(type(n))
    print(n)
    num = []
    sum = 0
    avg = 0
    num.append(n.split(','))
    num = num[0]
    for i in range(len(num)):
        num[i] = int(num[i])
    for i in range(len(num)):
        sum = num[i] + sum
    avg = sum / len(num)
    print(sum)
    print(avg)
