print('''
- 알고 리즘 : 어떤 문제 해결하기 위한 절차나 방법.
- 들여쓰기 : indent
- 변수 : variable
- 문자열 : string
''')

from bs4 import BeautifulSoup
import urllib.request

print('네이버 삼성전자 주식 가져오기')
# url = 'https://finance.naver.com/sise/'
page = '''
<ul class="lst_pop" id="popularItemList">
<li><em>1.</em><a href="/item/main.nhn?code=180640" onclick="clickcr(this,'boa.list','180640','1',event)">한진칼</a><span class="up">38,150</span><img alt="상승" src="https://ssl.pstatic.net/static/nfinance/ico_up.gif" width="7" height="6"></li>

<li><em>2.</em><a href="/item/main.nhn?code=005930" onclick="clickcr(this,'boa.list','005930','1',event)">삼성전자</a><span class="up">44,900</span><img alt="상승" src="https://ssl.pstatic.net/static/nfinance/ico_up.gif" width="7" height="6"></li>

<li><em>3.</em><a href="/item/main.nhn?code=020560" onclick="clickcr(this,'boa.list','020560','1',event)">아시아나항..</a><span class="dn">6,650</span><img alt="하락" src="https://ssl.pstatic.net/static/nfinance/ico_down.gif" width="7" height="6"></li>

<li><em>4.</em><a href="/item/main.nhn?code=207940" onclick="clickcr(this,'boa.list','207940','1',event)">삼성바이오..</a><span class="dn">346,000</span><img alt="하락" src="https://ssl.pstatic.net/static/nfinance/ico_down.gif" width="7" height="6"></li>

<li><em>5.</em><a href="/item/main.nhn?code=068270" onclick="clickcr(this,'boa.list','068270','1',event)">셀트리온</a><span class="dn">213,500</span><img alt="하락" src="https://ssl.pstatic.net/static/nfinance/ico_down.gif" width="7" height="6"></li>

<li><em>6.</em><a href="/item/main.nhn?code=078130" onclick="clickcr(this,'boa.list','078130','1',event)">국일제지</a><span class="dn">1,325</span><img alt="하락" src="https://ssl.pstatic.net/static/nfinance/ico_down.gif" width="7" height="6"></li>

<li><em>7.</em><a href="/item/main.nhn?code=000660" onclick="clickcr(this,'boa.list','000660','1',event)">SK하이닉스</a><span class="up">81,100</span><img alt="상승" src="https://ssl.pstatic.net/static/nfinance/ico_up.gif" width="7" height="6"></li>

<li><em>8.</em><a href="/item/main.nhn?code=18064K" onclick="clickcr(this,'boa.list','18064K','1',event)">한진칼우</a><span class="up">66,100</span><img alt="상승" src="https://ssl.pstatic.net/static/nfinance/ico_up.gif" width="7" height="6"></li>

<li><em>9.</em><a href="/item/main.nhn?code=086820" onclick="clickcr(this,'boa.list','086820','1',event)">바이오솔루..</a><span class="up">61,400</span><img alt="상승" src="https://ssl.pstatic.net/static/nfinance/ico_up.gif" width="7" height="6"></li>

<li><em>10.</em><a href="/item/main.nhn?code=003495" onclick="clickcr(this,'boa.list','003495','1',event)">대한항공우</a><span class="up">25,200</span><img alt="상승" src="https://ssl.pstatic.net/static/nfinance/ico_up.gif" width="7" height="6"></li>
</ul>
'''
# html = urllib.request.urlopen(page)

soup = BeautifulSoup(page,'html.parser')
# soup.select_one()
results = soup.select('ul#popularItemList > li > a')
for result in results:
	print(result.string)
