import os
import re

clear = lambda: os.system('clear')

data = "AS _34:AS11.23 @#$ %12^*"
exp = "\W, \w, [^A-z0-9_]"
txt='''\
\W : not word 워드가 아닌 것 = [^A-z0-9_]
\w : word 인 것 = [A-z0-9_]
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