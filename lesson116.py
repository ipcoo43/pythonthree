import math
import os
import re
'''

for a in lst:
	if a.find('__')>-1:
		lst.remove(a)
'''
lst = dir(math)
i=0
answer = ''
while answer != lst[i]:
	os.system('clear')
	answer = input('{} >> '.format(lst[i]))
	help('math'+'.'+lst[i])
	i += 1
