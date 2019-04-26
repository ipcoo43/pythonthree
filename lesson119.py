import os

lstA = ['abs(x)','int(x)','long(x)','float(x)','complex(re,im)','divmod(x,y) ','pow(x,y)']
lstB = ['x의 절대값','x를 int(정수)형으로 변환','x를 long형으로 변환','x를 float형으로 변환','실수부re와 허수부im를 갖는 복소수','(x/y, x%y) 쌍','x의 y승']

i=0
while i<len(lstA):
	os.system('clear')
	print('>>>',lstB[i])
	data = input('{} >> '.format(lstA[i]))
	print('>>>',lstB[i])
	if data == '': break
	i += 1

os.system('clear')
print('내장 수치 연산 함수를 학습 하였습니다.')