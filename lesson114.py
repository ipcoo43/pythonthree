#!/opt/conda/bin/python
import os
clear = lambda: os.system('clear')
clear()

print('''\
type(10)
type('10')
type(10.1)
''')

output = []
while True:
	input_data = input('>>> ')
	if input_data == "":
		break
	else:
		output.append(input_data)
for line in output:
	print(line)