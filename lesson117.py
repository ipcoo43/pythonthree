import keyword
import os

lst = keyword.kwlist
i=0
answer = ''
while answer != lst[i]:
	os.system('clear')
	answer = input('{} >> '.format(lst[i]))
	help(lst[i])
	i += 1