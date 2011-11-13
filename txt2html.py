#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, re

from handlers import HTMLRenderer
from parser import Parser
from rules import *

class Txt2HTMLParser(Parser):
    def __init__(self, handler):
        Parser.__init__(self, handler)

        ## ul, li 列表处理
        self.addRule(ListRule())
        self.addRule(ListItemRule())

        ## 文章标题处理
        self.addRule(TitleRule())

        ## 一级标题
        self.addRule(Header1Rule())

        ## 普通段落处理
        self.addRule(ParagraphRule())

        ###############################################################
        ##                        特殊标记处理
        ###############################################################
        
        ## 斜体
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        ## url
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        ## email
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-z]+)', 'mail')

        ## header
        ## self.addFilter(r'^=+(.+?)', 'header')

def main():
    h = HTMLRenderer()
    parser = Txt2HTMLParser(h)

    parser.parse(sys.stdin)
    
if __name__ == '__main__':
    main()
