#!/usr/bin/env python

# adapted from: 
# https://github.com/a5482pick/Python-Chrome-App-Native-Messaging/blob/master/Host/native-messaging-example-host
# this is a test

import sys
import struct
import traceback
import nativemessaging

import zerorpc

# assumes that main.py is running in the background
c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4001")

def send_message(message):
    message = nativemessaging.encode_message(message)
    nativemessaging.send_message(message)

def handle_message(message):
    c.websiteHandler(message)

def read_message():
    while 1:
        message = dict(nativemessaging.get_message())
        handle_message(message)

def main():
    
    read_message()


if __name__ == "__main__":
    main()



