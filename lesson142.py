import os
import re

clear = lambda: os.system('clear')

data = "<div>test</div><div>test2</div>"
exp = "<div>.+</div>, <div>.+?</div>"
txt='''\
r.*?, r.+?, r.??를 언제 사용 할 것 인가
<div>.+</div> : <div>에서 마지막 </div>가 사이의 문자가 선택됨 (탐욕적 수량자)
해결 방법으로 <div>.+?</div>을 사용함
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