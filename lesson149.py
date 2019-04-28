import os
import re

clear = lambda: os.system('clear')

data = "Ere iron was found or tree was test\n When young was mountain under test\nEre ring was made, or wrounght was woe, It walked the forests long test"
exp = "\A..., ...\Z, ^Ere, \AEre, test$, test\Z"
txt='''\
어떤 행에서 가장 앞쪽과 뒤쪽에 바운더리 지정
^,$와 유사하지만 조금에 차이가 있다.
\A... : 시작점의 경계(\A), 임의의 문자 3개(...), 시작점의 3개의 문자
...\Z : 끝난 지점의 경계(\Z), 임의의 문자 3개(...), 끝지점의 3개의 문자
^와 \A...의 차이 : ^Ere, \AEre   멀티 라인의 매치에서 차이 발생
$와 \Z...의 차이 : test$, test\Z 멀티 라인의 매치에서 차이 발생
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