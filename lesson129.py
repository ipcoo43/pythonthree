import os
import re

clear = lambda: os.system('clear')

data = "Regular expressions are powerful"
exp = ".은 모든 문자"
print(data)
while True:
	output = input('{} >>> '.format(exp))
	regex = re.compile(output)
	mo = regex.search(data)
	print(mo)
	if output == '':
		break