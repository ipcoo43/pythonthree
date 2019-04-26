#!/opt/conda/bin/python
import os
clear = lambda: os.system('clear')
clear()

print('''\
문제 : 문자열과 반복 횟수를 입력 받은 후 문자열을 반복 횟수 만큼 출력
a=int(input('문자열 = '))
b=int(input('반복횟수 = '))
for x in range(b):
  print(a.end="")
''')

a=input('a => ')
b=input('b => ')
c=input('c => ')
d=input('c => ')
print('a =',a)
print('b =',b)
print(c)
print(d)