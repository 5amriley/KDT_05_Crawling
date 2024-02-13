from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, 'html.parser')

# 등장인물의 이름: 녹색
nameList = soup.find_all('span', {'class': 'green'})
for name in nameList:
    print(name.string)

# 특정 단어 찾기
princeList = soup.find_all(string='the prince')
print(princeList)
print('the prince count: ', len(princeList))
