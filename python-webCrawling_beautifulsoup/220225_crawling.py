from email.mime import base
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


baseurl = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
plusUrl = input("검색어를 입력하세요.")

url = baseurl + urllib.parse.quote_plus(plusUrl)  # UTF -8  아스키코드로 변환
html = urllib.request.urlopen(url).read()  # html 가져옴
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='news_tit')


for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print("\n")
