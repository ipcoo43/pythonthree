import os

lstA = ['for','for','for','for','for','for','for','for','for']
lstB = ['for i in list','for i in range(len(list))','[expression for item in list if conditional]','[num * 3 for num in a if num % 2 == 0]','[x*y for x in range(2,10)]','[x for x in str]','[ x*2 for x in [x*2 for x in range(11)]]','[(x, y) for x in range(3) for y in range(3)]','for idx, key in enumerate(list)']

i=0
while i<len(lstA):
	os.system('clear')
	print('>>>',lstB[i])
	data = input('{} >> '.format(lstA[i]))
	print('>>>',lstB[i])
	if data == '': break
	i += 1

os.system('clear')
print('리스트 내표를 학습 하였습니다.')