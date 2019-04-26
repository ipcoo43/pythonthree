#!/opt/conda/bin/python
import os
clear = lambda: os.system('clear')
clear()

print('''\
문제 : 두 개의 숫자를 입력 받은 후 두 개의 숫자를 더한 값 출력
a=int(input('a = '))
b=int(input('b = '))
print('total : %d'%(a+b))
''')

a=input('a => ')
b=input('b => ')
c=input('c => ')
print('a =',a)
print('b =',b)
print(c)