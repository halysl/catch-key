# -*- coding:utf-8 -*-
 
import keylogger
import time

now = time.time()
done = lambda: time.time() > now + 60
def print_keys(t, modifiers, keys): 
    if keys:
        print("{}  {}".format(t, keys))
    else:
        for key, value in modifiers.items():
            if value:
                print("{}  {}".format(t, key))

keylogger.log(done, print_keys)
