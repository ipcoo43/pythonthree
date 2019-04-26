#!/opt/conda/bin/python
import os
clear = lambda: os.system('clear')
clear()

print('''\
문제 : 문자열 '720'를 정수형으로 변환하라. 정수 100을 문자열 '100'으로 변환
type('720')
type(int('720'))
type(100)
type(str(100))
''')

a=input('a => ')
b=input('b => ')
c=input('c => ')
d=input('d => ')
print(eval(a))
print(eval(b))
print(eval(c))
print(eval(d))