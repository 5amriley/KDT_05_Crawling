from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs)           # 전체 html 코드 가짐
print(bs.h1)        # 첫번째 h1 태그
print(bs.h1.string) # 첫번째 h1 태그의 문자열만 추출

print(bs.title)
print('title:', bs.title.stirng)
