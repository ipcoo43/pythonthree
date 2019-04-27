import os
import re

clear = lambda: os.system('clear')

data = "Monday Tuesday Friday"
exp = "(|)은 서브패턴의 or의 의미 => (on|ues|rida), (Mon|Tues|Fir)day, ..(id|esd|nd)ay"
print(data)
while True:
	output = input('{} >>> '.format(exp))
	regex = re.compile(output)
	a = regex.match(data)
	b = regex.search(data)
	c = regex.findall(data)
	print('mathch(문자열의 처음부터) :',a)
	print('search(문자열의 전체) :',b)
	print('findall(모든 문자열 리스트) :',c)
	if output == '':
		clear()
		break