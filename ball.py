import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%ED%94%84%EB%A1%9C%EC%95%BC%EA%B5%AC+%EC%88%9C%EC%9C%84"

res=requests.get(url).text

soup = BeautifulSoup(res,'html.parser')

picks = soup .select('#abtColl > div.coll_cont > div > div.tab_body > div:nth-of-type(1) > div > table > tbody > tr:nth-of-type(1) > td:nth-of-type(3)')

print(picks.text)