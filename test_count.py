# -*- coding:utf-8 -*-

"""
todo list:
1 读取文件
2 统计字符
3 输出信息
"""

import os
from io import StringIO
import count
import mock
from count import count_char, print_info


def test_read_file():
    """
    @test_func: read_file
    @func_param: None
    @test_desc: 检测是否可以读取文件
    """
    result = os.path.exists(count.file_name)
    assert result

def test_count_char():
    """
    @test_func: count_char()
    @func_param: data str
    @test_desc: 检测是否可以统计击打键盘数
    """
    data1 = 'a w d a c x w d a s d w j h n k a h n w d m a s n d e j h a d s b f k k u a w a s d l c j l k a j r w'
    data2 = 'right_shift right_shift left_ctrl left_ctrl right_ctrl'
    data = ' '.join([data1, data2])

    expect = {'a': 9, 'w': 6, 'd': 7, 'c': 2, 'x': 1, 's': 4, 'j': 4, 'h': 3, 'n': 3, 'k': 4, 'm': 1, 'e': 1, 'b': 1, 'f': 1, 'u': 1, 'l': 2, 'r': 1, 'right_shift': 2, 'left_ctrl': 2, 'right_ctrl': 1}
    actual = count.count_char(data)

    assert expect == actual

def test_print_info():
    """
    @test_func: print_info()
    @func_param: data dict
    @test_desc: 检测是否可以正确输出
    """
    dic = {'a': 12,'b': 31, 'c':48}
    expect = '当前输入字符统计：\n\nc:48\nb:31\na:12\n'
    
    with mock.patch('sys.stdout', new=StringIO()) as fake_out:
        print_info(dic)
        assert fake_out.getvalue() == expect
