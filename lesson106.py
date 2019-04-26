#!/opt/conda/bin/python
import os
clear = lambda: os.system('clear')
clear()

answer = ''
while answer != '서울':
	answer = input('♠ 대한민국의 수도는?  ')
	clear()
print('정답입니다.')
