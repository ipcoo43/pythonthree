import os
import re

clear = lambda: os.system('clear')

data = "--XX-@-XX-@@-XX-@@@-XX-@@@@-XX-@@-@@-"
exp = "-X?XX?X, -@?@?@?-"
txt='''\
수량자(? : 없거나 하나) 
-X?      : X?는 X가 없어도 되고 하나(?)여야하지만 여러개는 허용이 안됨
-X?X     : X?뒤에 X는 반드시 있어야 함 
-X?XX?   : X?X뒤에 X?는 없어도괴고 하나는 있어야함
-X?XX?X  : -X?XX?뒤에 X는 반드시 있어야 함
-@?@?@?- : - 뒤에 @? 0~1
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