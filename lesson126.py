import os
clear = lambda: os.system('clear')
clear()

import re

data = "Hello, world!"
exp = "Hello, world"
print(data)
output = input('{} >>> '.format(exp))
regex = re.compile(output)
mo = regex.search(data).group()
print(mo)