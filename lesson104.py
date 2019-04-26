#!/opt/conda/bin/python
import os
clear = lambda: os.system('clear')
clear()

import re

#data = input('>>> ')
data = "abc 33 bb 1 dd"
regex = re.compile("^[a-zA-Z]*$")
mo = regex.search(data)
print(mo)
