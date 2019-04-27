import os
import re

clear = lambda: os.system('clear')

data = "who is who"
exp = "^who 대상의 시작, who$ 대상의 끝"
print(data)
while True:
	output = input('{} >>> '.format(exp))
	regex = re.compile(output)
	mo = regex.search(data)
	print(mo)
	if output == '':
		break