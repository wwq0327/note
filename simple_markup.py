#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    simple_markup
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-10-17
    :author: wwq0327 <wwq0327@gmail.com>
    :license: LGPL 2 or later (see README/COPYING/LICENSE)

"""

import sys, re
from util import *

print '<html><head><title>...</title></head><body>'

title = True

for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title = False
    else:
        print '<p>'
        print block
        print '</p>'

print '</body></html>'
