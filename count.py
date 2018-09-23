# -*- coding:utf-8 -*-

import os

from recording import curr_path, file_name


def read_file():
    """
    @desc 读取日志文件，获得输入字符信息，编成字符串返回
    @return str
    """
    data = []
    file_path = os.path.join(curr_path, file_name)
    with open(file_path, 'r') as f:
        for line in f.readlines():
            data.append(line.strip('\n'))
    
    result = []
    for d in data:
        result.append(d.split(' ')[-1])

    return ' '.join(result)
        

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
