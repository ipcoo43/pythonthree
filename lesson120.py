import os

lstA = ['시퀀스 자료형이란?','시퀀스 자료형이란?','시퀀스 자료형이란?','종류','공통 연산','공통 연산','공통 연산','공통 연산','공통 연산','공통 연산']
lstB = ['여러 객체를 저장','각 객체들은 순서를 갖는다','각 객체들은 첨자를 이용하여 참조가능 하다','list, tuple, string','인덱싱(indexing) [1]','슬라이싱(slicing) [1:4]','연결하기 str1 + str2','반복하기 str1 * 4','멤버십 테스트 "a" in str','길이 정보 len(str)']

i=0
while i<len(lstA):
	os.system('clear')
	print('>>>',lstB[i])
	data = input('{} >> '.format(lstA[i]))
	print('>>>',lstB[i])
	if data == '': break
	i += 1

os.system('clear')
print('시퀀스 자료형을 학습 하였습니다.')