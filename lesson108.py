#!/opt/conda/bin/python
import os
import sys
clear = lambda: os.system('clear')
clear()

print('''\
string = []
while True:
  input_data = input()
  if input_data =="":
    break
  else:
    string.append(input_data)
for line in string:
  print(line)
''')

# string = sys.stdin.readlines()
# print(string)

string = []
while True:
	input_data = input('>>> ')
	if input_data =="":
		break
	else:
		string.append(input_data)
clear()
for line in string:
	print(line)