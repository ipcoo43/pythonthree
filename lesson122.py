import os

lstA = ['append','insert','index','count','sort','reverse','remove','pop','extend']
lstB = ['자료를 리스트 끝에 추가','자료를 지정된 위치에 삽입','요소 검색','요소 개수 알아내기','리스트 정렬','자료 순서 바꾸기','지정 자료 값 한 개 삭제','리스트의 마지막 값을 읽어내고 삭제','리스트를 추가']

i=0
while i<len(lstA):
	os.system('clear')
	print('>>>',lstB[i])
	data = input('{} >> '.format(lstA[i]))
	print('>>>',lstB[i])
	if data == '': break
	i += 1

os.system('clear')
print('리스트 메소드를 학습 하였습니다.')