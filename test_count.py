# -*- coding:utf-8 -*-

"""
todo list:
1 读取文件
2 统计字符
3 输出信息
"""

import count
import os

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
    pass

def test_print_info():
    pass