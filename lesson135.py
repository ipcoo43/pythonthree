import os
import re

clear = lambda: os.system('clear')

data = "aabc abc bc"
exp = "a*b, a+b, a?b"
txt='''\
수량자(어떠한 패턴이 얼마 만큼 등장하는 숫자) 
* : 0~여러개, 있을 수도 있고 없을 수도 있다.
+ : 1~여러개, 하나 이상 이어야 한다.
? : 없거나 하나인 경우
b를 기준으로 앞으로 읽을 것
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