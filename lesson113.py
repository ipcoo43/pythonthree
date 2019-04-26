#!/opt/conda/bin/python
import os
clear = lambda: os.system('clear')
clear()

print('''\
문제 : Integer, String, Float 타입축력
a=10
b='10'
c=10.1
''')

a=int(input('a => '))
b=input('b => ')
c=float(input('c => '))
print(type(a))
print(type(b))
print(type(c))