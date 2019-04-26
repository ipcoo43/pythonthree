# from pprint import pprint
# pprint(lst, indent=4, width=20)


lst = ['abs','all','any','ascii','bin','bool','breakpoint','bytearray','bytes','callable','chr','@classmethod','compile','complex','delattr','dict','dir','divmod','enumerate','eval','exec','filter','float','format','frozenset','getattr','globals','hasattr','hash','help','hex','id','input','int','isinstance','issubclass','iter','len','list','locals','map','max','max','memoryview','min','next','object','oct','open','ord','pow','print','property','range','repr','reversed','round','set','setattr','slice','sorted','@staticmethod','str','sum','super','tuple','type','vars','zip']

import os

answer = ''
i=0
while answer != lst[i]:
	os.system('clear')
	answer = input('{} >> '.format(lst[i]))
	help(lst[i])
	i += 1

#	print('{} >> '.format(lst[i]))