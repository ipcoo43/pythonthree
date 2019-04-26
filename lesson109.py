#!/opt/conda/bin/python
import os
import sys
clear = lambda: os.system('clear')
clear()

print('''\
print('%.2f'%(3.141592))
''')
input_data=input('>>> ')
print(eval(input_data))