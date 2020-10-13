# A parent process sends n strings to a child process. The child process displays all the
# palindromes. Implement this using Pipes.

import os
import time


def reverse(straight):
    return 'c~' + ''.join(reversed(straight))


def display_if_palindrome(input_str):
    if input_str == reverse(input_str):
        print(input_str)


if __name__ == '__main__':
    print('\nQuestion\n')
    print('A parent process sends n strings to a child process. The child process displays all the palindromes. '
          'Implement this using Pipes.\n')

    # Create pipe. [ We'll be writing from the parent process and reading from the child process. ]
    r, w = os.pipe()

    # Get the number of strings to send.
    n = int(input("How many strings? "))

    # Store the strings in an array.
    strings = []
    for _ in range(n):
        strings.append(input("Enter string: "))

    # Encode the strings for sending through pipe.
    message = '~'.join(strings)
    message = message.encode()

    print('\nCreating child process.')
    print('Parent -> p~')
    print('Child -> c~')
    print('=====================================================\n')
    # Create child process.
    pid = os.fork()

    # Process with pid > 0 is the parent process.
    if pid > 0:
        # Close the read pipe.
        os.close(r)

        print("p~Parent process sending the strings...")
        # Writing into the pipe.
        os.write(w, message)
        print('p~Strings Sent.')
        # Wait one second so that the output doesn't look weird.
        time.sleep(1)

    else:
        # Close the write pipe.
        os.close(w)

        print("\nc~Child process waiting for messages.")
        r = os.fdopen(r)
        msg = r.read()
        print('c~Message received.')
        print('c~Printing palindromes...')
        for s in msg.split('~'):
            display_if_palindrome(s)
