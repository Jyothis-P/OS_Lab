import os

r, w = os.pipe()

pid = os.fork()

if pid > 0:

    os.close(r)

    print("Parent process is writing")
    text = "hai"
    os.write(w, text.encode())


else:

    os.close(w)

    print("\nChild Process is reading")
    r = os.fdopen(r)
    print("Read text:", r.read())
