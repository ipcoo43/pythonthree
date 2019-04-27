import os
import re

clear = lambda: os.system('clear')

data = "One ring to bring them all and in the darkness bind them"
exp = ".{5}, [els]{1,3}, [a-z]{3,}"
txt='''\
수량자({값} : {} 사이에 값이 수량을 의미) 
.{5} : .(어떤 문자도 상관 없음)에 {5} => 어떤 글자든 5글자 여야 한다.
[els]{1,3} : [els] esl중 한글자가 {1,3} 1 이상 3이하 여야 한다.
[a-z]{3,} : [a-z]는 소문자 a-z 중 한글자가 {3,} 3이상의 모든 것
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