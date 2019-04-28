import os
import re

clear = lambda: os.system('clear')

data = "AAAX---aaax---111"
exp = "\w+(?=X), \w+, \w+(?=\w)"
txt='''\
\w+ : 문자(\w),1이상(+)
(?=X) : 뒤에 따라오는(?=) X라는 것을 문자열 검색에 쓰지만 매치는 되지 않음
\w+(?=X) : AAAX에서 문자들이 매치되지만 AAA만 매치됨 X는 제외 시킴
X는 X 앞의 단어 AAA를 찾는데는 기여했지만 자신은 매치되지 않음
\w+ : (?=X)없이 하게되면 AAAX,aaax,111과 매치됨
\w+(?=\w) : AAA,aaa,11과 매치됨
(?=\w) : 조건에 문자를 만족시키면 자신은 찾는데만 기여하고 매치는 안됨
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