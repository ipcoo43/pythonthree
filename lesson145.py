import os
import re

clear = lambda: os.system('clear')

data = "Page 123; published: 1234 id=12#24@112"
exp = "\d, \D, [0-9]"
txt='''\
\d : digit(0-9) 숫자 매치 = [0-9]
\D : digit(0-9) 숫자 아닌 것과 매치
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