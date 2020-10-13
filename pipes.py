import os

print('Python program to explain os.pipe() method ')

# Create a pipe
r, w = os.pipe()

# Create a child process
pid = os.fork()

# pid greater than 0 represents
# the parent process
if pid > 0:
    print('Parent:', pid)

    # This is the parent process
    # Closes file descriptor r
    os.close(r)

    # Write some text to file descriptor w
    print("Parent process is writing")
    text = b"Hello child process"
    os.write(w, text)
    print("Written text:", text.decode())


else:
    print('Child:', pid)

    # This is the parent process
    # Closes file descriptor w
    os.close(w)

    # Read the text written by parent process
    print("\nChild Process is reading")
    r = os.fdopen(r)
    print("Read text:", r.read())
