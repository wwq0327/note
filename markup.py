#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, re
from handlers import *
from util import *
from rules import *

class Parser:
    """语法分析器读取文本文件、应用规则并且控制处理程序"""

    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last: break
        self.handler.end('document')

class BasicTextParser(Parser):
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())                    ## ui 表列
        self.addRule(ListItemRule())                ## li 列表子项
        self.addRule(TitleRule())                   ## 标题
        self.addRule(HeadingRule())                 ## 标题头
        self.addRule(ParagraphRule())               ## 段落

        ## 斜体
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        ## url
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        ## email
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-z]+)', 'mail')

if __name__ == '__main__':
    handler = HTMLRenderer()
    parser = BasicTextParser(handler)

    parser.parse(sys.stdin)
