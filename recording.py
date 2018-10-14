# -*- coding:utf-8 -*-

import logging
import os
import sys
import time

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
        pass
    elif system == 'darwin':
        pass
    else:
        pass


def start_keylogger(t, modifiers, keys):
    pass


if __name__ == "__main__":
    pass
