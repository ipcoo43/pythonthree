import os
import re

clear = lambda: os.system('clear')

data = "How do you do?"
exp = "[]은 문자 하나에 해당 => [oyu], [dH]., [owy][yow]"
print(data)
while True:
	output = input('{} >>> '.format(exp))
	regex = re.compile(output)
	mo = regex.search(data)
	print(mo)
	if output == '':
		break