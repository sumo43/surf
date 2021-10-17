#!/usr/bin/env python

# adapted from: 
# https://github.com/a5482pick/Python-Chrome-App-Native-Messaging/blob/master/Host/native-messaging-example-host
# this is a test

import sys
import struct


def read_message():
    message_number = 0
    while 1:
        # Read the message length (first 4 bytes).
        text_length_bytes = sys.stdin.read(4)
        if len(text_length_bytes) == 0:
            if queue:
                queue.put(None)
            sys.exit(0)
            # Unpack message length as 4 byte integer.
            text_length = struct.unpack('i', text_length_bytes)[0]
            # Read the text (JSON object) of the message.
            text = sys.stdin.read(text_length).decode('utf-8')
            if queue:
                queue.put(text)
        else:
            # In headless mode just send an echo message back.
            send_message('{"echo": %s}' % text)



def Main():
    read_message()


if __name__ == "__main__":
    Main()



