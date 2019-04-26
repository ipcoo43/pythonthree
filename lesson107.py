#!/opt/conda/bin/python
import os
clear = lambda: os.system('clear')
clear()

print('''
[ 문제 ]
	◐ 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램 작성
[ 입력 ] 
	◐ 첫째 줄에 A와 B가 주어진다(0<A, B<10)
[ 출력 ]
	a,b=map(int,input().split())
	print(a+b)
''')

while True:
	output = input('>>> ')
	if output == 'y':
		break
	else:
		clear()
		print('>>>',output)
