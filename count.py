# -*- coding:utf-8 -*-

import os

from recording import curr_path, file_name


def read_file():
    data = []
    file_path = os.path.join(curr_path, file_name)
    with open(file_path, 'r') as f:
        for line in f.readlines():
            data.append(line)

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

if __name__ == "__main__":
    read_file()
