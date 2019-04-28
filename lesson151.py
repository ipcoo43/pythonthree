import os
import re

clear = lambda : os.system('clear')

while True:
	try:
		data = input('◈ source >>> ')
		output = input('◈  regex >>> ')
		regex = re.compile(output)
		a = regex.search(data)
		b = regex.findall(data)
		print('search  :',a)
		print('findall :',b)
		if data == '':
			clear()
		if output == 'q':
			clear()
			break
	except:
		clear()
	