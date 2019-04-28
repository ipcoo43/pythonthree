import os
import re

clear = lambda: os.system('clear')

data = "A1 B2 c3 d_4 e:5 ffGG77--___--"
exp = "\w, \w*, [a-z]\w*, \w{5}, [A-z0-9_]"
txt='''\
\w : word(단어) = alpha+numeric+_ = [A-z0-9_]
\w* : 0 이상의 단어, 공백은 워드 안에 포함 않됨
[a-z]\w* : a-z까지 문자가 0 이상인 단어
\w{5} : 문자 5개
[A-z0-9_] : \w와 같은 의미
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