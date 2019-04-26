import os

lstA = ['abs(x)','int(x)','long(x)','float(x)','complex(re,im)','divmod(x, y) ','pow(x, y)']
lstB = ['x의 절대값','x를 int(정수)형으로 변환','x를 long형으로 변환','x를 float형으로 변환','실수부re와 허수부im를 갖는 복소수','(x/y, x%y) 쌍','x의 y승']

i=0
answer = ''
while answer != lstA[i]:
	os.system('clear')
	print('>>>',lstB[i])
	answer = input('{} >> '.format(lstA[i]))
	i += 1