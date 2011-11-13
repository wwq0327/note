#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    util
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-10-17
    :author: wwq0327 <wwq0327@gmail.com>
    :license: LGPL 2 or later (see README/COPYING/LICENSE)

"""

def lines(file):
    '''在文本的最后一行加入一个空行'''
    
    for line in file: yield line
    yield '\n'

def blocks(file):
    '''收集遇到的所有行，直接遇到一个空行，然后返回已经收集到的行。
    那些返回的行就是一个代码块
    '''
    
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
