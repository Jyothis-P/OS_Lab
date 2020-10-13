import os

print('Python program to explain os.pipe() method ')

r, w = os.pipe()

n = int(input("How many strings? "))
strings = []
for _ in range(n):
    strings.append(input("Enter string: "))

message = '~'.join(strings)
message = message.encode()

pid = os.fork()

if pid > 0:
    print('Parent:', pid)

    os.close(r)

    print("Parent process is writing")
    os.write(w, message)
    print("Written text:", message.decode())


else:
    print('Child:', pid)

    os.close(w)

    print("\nChild Process is reading")
    r = os.fdopen(r)
    msg = r.read()
    print("Read text:", msg)
