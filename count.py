# -*- coding:utf-8 -*-

from recording import curr_path, file_name


def read_file():
    pass

def count_char(data):
    data = data.split(' ')
    dic = dict()

    for i in data:
        if not dic.get(i, ''):
            dic[i] = 1
        else:
            dic[i] += 1
    return dic

def print_info():
    pass