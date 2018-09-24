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

def print_info(dic):
    result = sorted(dic.items(), key=lambda item:item[1], reverse=True)
    first_line = '当前输入字符统计：\n'
    lines = []
    for i in result:
        line = ''.join([i[0], ':', str(i[1])])
        lines.append(line)
    
    print(first_line)
    for line in lines:
        print(line)

if __name__ == "__main__":
    data = read_file()
    result = count_char(data)
    print_info(result)
