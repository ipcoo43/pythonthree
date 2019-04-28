import os
import re

clear = lambda: os.system('clear')

data = "Ere iron was fond or tree was hewn,\n When young was mountain under moon;\nEre ring was made, or wrounght was woe,\n It walked the forests long ago."
exp = "\\b\\w, \\w\\b, \\b\\w\\b, \\b\\w+\\b"
txt='''\
\\b\w : 단어의 시작과 매치
\\w\\b : 단의의 끝과 매치
\\b\\w\\b : 단어가 한개 인것과 매치
\\b\\w+\\b : 단어가 한개 이상인 것과 매치
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