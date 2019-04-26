import re
import os 
clear=lambda:os.system('clear')

clear()
#data = '2*3+(4-2)*2/2+(10-2)'
while True:
    data = input('>>> ')
    rex = re.compile('[-|+|*|/|0-9|(|)|\s|.]*')
    out_a = rex.search(data).group()
    out_b = eval(rex.search(data).group())
    print('♣ ♣ %s = %0.2f'%(out_a,out_b))
    if data == '2469':
        break
    elif data == '7943':
        clear()
        continue