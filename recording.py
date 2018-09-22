# -*- coding:utf-8 -*-

import keylogger
import time

now = time.time()
time = lambda: time.time() > now + 60 * 60 *24

def print_keys(t, modifiers, keys): 
    if keys:
        print("{}  {}".format(t, keys))
    else:
        for key, value in modifiers.items():
            if value:
                print("{}  {}".format(t, key))

def recoding_keys(t, modifiers, keys):
    pass

keylogger.log(time, print_keys)