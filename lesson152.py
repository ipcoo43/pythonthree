import re
import urllib.request

url = 'http://goo.gl/U7mSQl'
html = urllib.request.urlopen(url)
html_contents = str(html.read())

id_results = re.findall("[A-Za-z0-9]+\*\*\*",html_contents)

res = ''
with open('./test.txt','w',encoding='utf-8') as fp:
	for result in id_results:
		res += result
		res += '\n'
	fp.write(res)

with open('./test.txt','r',encoding='utf-8') as fp:
	print(fp.read())