import os
import re

clear = lambda: os.system('clear')

data = "ABCDEFGHIHKLMNOPQRSTUVWXYZabcedfghijklmnopqrstuvwxyz0123456789"
exp = "[^]은 []속에서 ^은 not의 의미 => [^CDghi45], [^W-Z]"
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
		break