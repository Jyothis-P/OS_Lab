# A parent process sends n strings to a child process. The child process displays all the
# palindromes. Implement this using Pipes.

import os
import time


def reverse(straight):
    return straight[::-1]


def display_if_palindrome(input_str):
    if input_str == reverse(input_str):
        print(input_str)


if __name__ == '__main__':

    # Create pipe. [ We'll be writing from the parent process and reading from the child process. ]
    r, w = os.pipe()

    # Get the number of strings to send.
    n = int(input("Enter number of strings: "))

    # Store the strings in an array.
    strings = []
    for _ in range(n):
        strings.append(input(f'Enter string {_ + 1}: '))

    # Encode the strings for sending through pipe.
    message = '~'.join(strings)
    message = message.encode()

    print("")
    # Create child process.
    pid = os.fork()

    # Process with pid > 0 is the parent process.
    if pid > 0:
        # Close the read pipe.
        os.close(r)

        print("Parent process writing to pipe.")
        # Writing into the pipe.
        os.write(w, message)
        # Wait one second so that the output doesn't look weird.
        print("")
        time.sleep(1)

    else:
        # Close the write pipe.
        os.close(w)

        r = os.fdopen(r)
        msg = r.read()
        print('Message received by child process.')
        print('Palindromes are...')
        for s in msg.split('~'):
            display_if_palindrome(s)
        print("")
