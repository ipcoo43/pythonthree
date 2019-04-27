import os
import re

clear = lambda: os.system('clear')

data = "One ring to bring them all and in the darkness bind them"
exp = "r.*, r.*?, r.+, r.+?, r.?, r.??"
txt='''\
수량자(수량자+? : *?(0), +?(1), ??(0)) 
r.*  : .(어떤 문자가 하나 와도) *(0 이상), r뒤에있는 문자 모두 선택됨
*? : 수량자+?는 의미가 달라진다. *?는 0의 의미가 됨
.*? : .에 의미가 *?(0, 즉 사용안함)로 인하여 사용되지 않게 됨
r.*? : .*?의 의미가 0으로 r문자만 남게 됨
r.+ : r 뒤에 문자가 오는데(.) 하나 이상이어야(+) 한다
r.+? : .+?의 의미가 1로 r+글자 하나만 남게 됨 
r.? : r 뒤에 글자가 0 또는 1의 글자
r.?? : .??의 의미가 0으로 r문자만 남게 됨
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