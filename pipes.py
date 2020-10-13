import os


def reverse(straight):
    return "".join(reversed(straight))


def display_if_palindrome(input_str):
    if input_str == reverse(input_str):
        print(input_str)


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
    os.waitpid(pid)


else:
    print('Child:', pid)

    os.close(w)

    print("\nChild Process is reading")
    r = os.fdopen(r)
    msg = r.read()
    for s in msg.split('~'):
        display_if_palindrome(s)
    print("Read text:", msg)
