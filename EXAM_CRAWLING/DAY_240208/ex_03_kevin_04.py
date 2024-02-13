# 링크간 무작위 이동하기

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

pages = set()
count = 0

def getLinks(pageUrl):
    global pages
    global count
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 새로운 페이지 발견
                newPage = link.attrs['href']
                count += 1
                print(f'[{count}]: {newPage}'.format(count, newPage))
                pages.add(newPage)  # 세트에 추가
                getLinks(newPage)   # 재귀 호출

# 에러 처리를 안 해줬기 때문에 실행 되던 중 에러 발생
getLinks('')
