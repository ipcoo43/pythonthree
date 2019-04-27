import os
import re

clear = lambda: os.system('clear')

data = "-@-***--'*'--**-@-"
exp = ".*, -A*-, [-@]*"
txt='''\
수량자(어떠한 패턴이 얼마 만큼 등장하는 숫자) 
.* : *는 0~여러개, *앞에 점이 붙어 있어 . 모든 텍스트
-A*- : 뒤에있는 -앞에 *(0~여러개) A가 있어도 되고 없어도 됨 
[-@]* : []는 한글자 후보군 지정,[-@]는 -나 @가 있다면, *표가 붙어서
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