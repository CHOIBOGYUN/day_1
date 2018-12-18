import requests
from bs4 import BeautifulSoup


url = "http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum"
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')
trs = soup.select("#asiaBody > table > tbody")

print(trs)


'''for tr in trs:
    print(tr.select_one("td.name a").text)
    print(tr.select_one("td:nth-of-type(2)").text)'''

#print(table)

# picks = soup .select('#asiaBody > table > tbody > tr:nth-child(2) > td.name')

# print(picks)

