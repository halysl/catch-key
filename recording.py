# -*- coding:utf-8 -*-

import logging
import os
import sys
import time
import imp

curr_path = os.path.dirname(os.path.abspath(__file__))
file_name = 'catch_key.log'

def get_logger():
    fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
    datefmt = "%a %d %b %Y %H:%M:%S"
    formatter = logging.Formatter(fmt, datefmt)

    filepath = os.path.join(curr_path, file_name)
    fh = logging.FileHandler(filepath, mode='a', encoding=None, delay=False)
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)

    logger_name = 'Catch-Key'
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logger.addHandler(fh)
    
    return logger


logger = get_logger()


def define_system():
    system = sys.platform
    return system


def install_keylogger(system):
    if system == 'linux':
        try:
            imp.find_module('python-xlib')
            found = True
        except Exception:
            found = False
        can_be_use = os.path.exists('../Keylogger/linux/keylogger.py')
    elif system == 'darwin':
        can_be_use = os.path.exists('/usr/local/bin/keylogger')
    else:
        pass
    
    if can_be_use:
        pass
    else:
        if system == 'linux':
            if not found:
                print('请安装python-xlib库\npip install python-xlib')
                sys.exit(-1)
        elif system == 'darwin':
            print('请编译keylogger\ncd Keylogger/mac\nmake && make install')
            sys.exit(-1)
        else:
            print('暂不操作')
            sys.exit(-1)


def start_keylogger():
    logger.info('process to run...')


if __name__ == "__main__":
    system = define_system()
    install_keylogger(system)
    start_keylogger()
