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
    n = r.read()
    sum = 0
    avg = 0
    num = n.split(',')
    num = num[0]
    for i in range(len(num)):
        num[i] = int(num[i])
    for i in range(len(num)):
        sum = num[i] + sum
    avg = sum / len(num)
    print(sum)
    print(avg)
