import os
import re

clear = lambda: os.system('clear')

data = "ABCDEFGHIHKLMNOPQRSTUVWXYZabcedfghijklmnopqrstuvwxyz0123456789"
exp = "[-]은 에서 까지 => [C-K], [a-d], [2-6], [C-Ka-d2-6]"
print(data)
while True:
	output = input('{} >>> '.format(exp))
	regex = re.compile(output)
	mo = regex.search(data)
	print(mo)
	if output == '':
		break