import os

lstA = ['대문자로 변경','소문자로 변경','대문자는 소문자로, 소문자는 대문자로 변경','첫 문자를 대문자로 변경','각 단어의 첫 글자를 대문자로 변경','문자열 양쪽 끝을 자른다. 제거할 문자를 인자로 전달 (디폴트는 공백)','문자열 왼쪽을 자름','문자열 오른쪽을 자름','문자열 특정 부분을 변경 (대체)','틀(포맷)을 만들어 놓고 문자열을 생성','리스트 같은 iterable 인자를 전달하여 문자열로 연결','문자열 가운데 정렬','문자열 왼쪽 정렬','문자열 오늘쪽 정렬','전달한 문자로 문자열을 나눔(분리), 결과는 튜플(구분자도 포함)','뒤에서 부터 전달한 인자로 문자열을 나눔','전달한 문자로 문자열을 나눔, 결과는 리스트(구분자 포함 안됨)','뒤에서 부터 전달한 문자로 문자열을 나눔','라인 단위로 문자열을 나눔','알파벳 또는 숫자인가?','알파벳인가?','숫자(decimal,10진수)인가?','숫자(digit,10진수)인가?','식별자로 사용 가능한가?','소문자인가?','숫자인가?','공백인가?','title 형식인가?','대문자인가?','특정 단어(문자열)의 수를 구함','특정 단어로 시작하는지 확인','특정 단어로 끝나는지 확인','특정 단어를 찾아 인덱스를 리턴 (없으면 -1을 리턴)','뒤에서부터 특정 단어를 찾아 인덱스를 리턴','특정 단어가 있는지 없는지 확인 가능 (True, False)','find와 동일하지만 없을 때 예외를 발생시킴','rfind와 동일하지만 없을 때 예외를 발생시킴']
lstB = ['upper()','lower()','swapcase()','capitalize()','title()','strip()','lstrip()','rstrip()','replace(a,b)','format()','"&".join()','center()','ljust()','rjust()','partition()','rpartition()','split()','rsplit()','splitlines()','isalnum()','isalpha()','isdecimal()','isdigit()','isidentifier() ','islower()','isnumeric()','isspace()','istitle()','isupper()','count()','startswith()','endswith()','find()','rfind()','in, not in','index()','rindex()']

i=0
while i<len(lstA):
	os.system('clear')
	print('>>>',lstB[i])
	data = input('{} >> '.format(lstA[i]))
	print('>>>',lstB[i])
	if data == '': break
	i += 1

os.system('clear')
print('문자열 객체 메소드를 학습 하였습니다.')