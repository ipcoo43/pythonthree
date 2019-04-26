import os
os.system('clear')
while True:
	try:
		data = input('>>> ')
	except:
		pass
	else:
		if data == '':
			break
		elif != data.isdigit():
			print('>>>', data)
		else:
			print('>>>', eval(data))
