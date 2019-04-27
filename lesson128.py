import os
import re

clear = lambda: os.system('clear')

data = "$12$ \-\ $25$"
exp = "^$,\$,^\$,\$$,\\\\"
print(data)
while True:
	output = input('{} >>> '.format(exp))
	regex = re.compile(output)
	mo = regex.search(data)
	print(mo)
	if output == '':
		break