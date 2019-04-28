import os
import re

clear = lambda: os.system('clear')

data = "cat concat"
exp = "\\bcat, cat\\b"
txt='''\
\\bcat : 앞에있는 cat만 매치
cat\\b : 앞과 뒤의 cat와 매치
'''
print(data)
print(txt)
while True:
	output = input('{} >>> '.format(exp))
	regex = re.compile(output)
	a = regex.search(data)
	b = regex.findall(data)
	print('search  :',a)
	print('findall :',b)
	if output == '':
		clear()
		break