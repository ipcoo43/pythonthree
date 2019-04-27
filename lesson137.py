import os
import re

clear = lambda: os.system('clear')

data = "-@@@-* **--'*'--* **-@@@-"
exp = "\*+, -@+-, [^ ]+"
txt='''\
수량자(+ : 하나이상의 여러개) 
\*+  : \는 뒤에따라오는 *를 수량자가아니 문자로 인식, 문자*가 뒤에오는 +로 하나 이상을 의미
-@+- : 앞- 뒤-가 반드시 와야하고, @은 뒤에 +로인해서 하나 이상이어야 한다.
[^ ]+ : 공백이 아닌 것이([^ ]) 하나 이상(+)일 때, 즉, 공백 빼고 나머지 선택
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