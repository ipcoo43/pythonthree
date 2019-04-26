#!/opt/conda/bin/python
import os
clear = lambda: os.system('clear')
clear()

import re

#data = input('>>> ')
data = "302+125*9-4/2"
regex = re.compile("([0-9]*)([-|+|*|/]*)([0-9]*)")
mo = regex.search(data)
print(mo.group())


regex = re.compile('([0-9]+)[ \t]*([+-/*])[ \t]*([0-9]+)')
mo = regex.search(data)
print(mo.group())

