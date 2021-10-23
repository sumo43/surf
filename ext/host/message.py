#!/usr/bin/env python

# adapted from: 
# https://github.com/a5482pick/Python-Chrome-App-Native-Messaging/blob/master/Host/native-messaging-example-host
# this is a test

import sys
import struct
import traceback
import nativemessaging

def send_message(message):
    message = nativemessaging.encode_message(message)
    nativemessaging.send_message(message)

def read_message():
    while 1:
        message = nativemessaging.get_message()
        with open('file.txt', 'w') as f:
            f.write(str(message))





def main():
    
    read_message()


if __name__ == "__main__":
    main()



