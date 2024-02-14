'''
    파이썬과 통합 : 예제 #2
    위키피디아의 자료를 MySQL에 저장
    - 실행하면 끝없이 돌아가므로, 콘솔창에서 ctrl + c 를 입력해서 실행을 중지시켜야 한다.
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re

conn = pymysql.connect(host='localhost', user='root',
                       password='2018', db='scraping', charset='utf8')

cur = conn.cursor()
random.seed(None)


def store(title, content):
    ''' pages 테이블의 title, content 필드에 데이터 추가'''
    cur.execute('insert into pages (title, content) values (%s, %s)', (title, content))
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org' + articleUrl)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1').text
    content = bs.find('div', {'id': 'mw-content-text'}).find('p').text

    # find()로 검색된 데이터를 데이터베이스에 저장
    store(title, content)
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()
