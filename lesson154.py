import re
import urllib.request

base_url = 'http://tangra.cs.yale.edu/clair/bib2html/radev-bib.html'
html = urllib.request.urlopen(base_url)
html_contents = str(html.read().decode('utf-8'))

url_list = re.findall('(http)(.+)(pdf)', html_contents)
for url in url_list:
	file_name = "".join(url)
	# print(file_name)
	# full_url = base_url + file_name
	# fname, header = urllib.request.urlretrieve(full_url, file_name)
	urllib.request.urlretrieve(file_name)
	print('End Download')