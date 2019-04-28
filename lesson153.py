import re
import urllib.request

url = 'https://www.google.com/googlebooks/uspto-patents-grants-text.html'
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode('utf8'))

url_list = re.findall('(http)(.+)(zip)', html_contents)

with open('./test1.txt','w',encoding='utf-8') as fp:
	for url in url_list:
		fp.write("".join(url)+'\n')

with open('./test1.txt','r',encoding='utf-8') as fp:
	print(fp.read())