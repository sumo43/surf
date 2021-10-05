#!/usr/bin/env python



# adapted from: 
# https://github.com/a5482pick/Python-Chrome-App-Native-Messaging/blob/master/Host/native-messaging-example-host
# this is a test

import sys
import struct

def read_message():
    while True:

        text_length_bytes = sys.stdin.read(4)
        if len(text_length_bytes) == 0:
            print("text length is none")
            sys.exit(0)

        # Unpack message length as 4 byte integer
        text_length = struct.unpack('i', text_length_bytes)[0]

        # Read the text (JSON object) of the message.
        text = sys.stdin.read(text_length).decode('utf-8')


def Main():
    read_message()


if __name__ == "__main__":
    Main()



