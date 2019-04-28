import os
import re

clear = lambda: os.system('clear')

data = "cat concat"
exp = "\B., \B.\B"
txt='''\
\B. : \\b.와 반대 매치
\B.\B : 바운더리가 안닌 것 a와 매치
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