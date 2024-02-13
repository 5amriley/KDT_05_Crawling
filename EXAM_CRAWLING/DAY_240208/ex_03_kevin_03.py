# 링크간 무작위 이동하기

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
# datetime
# random.seed(datetime.datetime.now())
random.seed(None)   # Python 3.9 이상

def getLinks(articleUrl):
    html = urlopen('https://en.wikipedia.org' + articleUrl)
    bs = BeautifulSoup(html, 'html.parser')
    bodyContent = bs.find('div', {'id': 'bodyContent'})
    wikiUrl = bodyContent.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    return wikiUrl  # 리스트 형태


links = getLinks('/wiki/Kevin_Bacon')
print(type(links))
print('links 길이: ', len(links))
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)