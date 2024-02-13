'''
    24/02/07 과제 1
    샌프란시스코 날씨 웹사이트에서 원하는 정보 크롤링하기
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup


def scraping_use_find(soup):
    bs_id = soup.find('ul', {'id': 'seven-day-forecast-list'})     # 목표 코드에 가장 가까운 id
    print('National Weather Service Scraping')
    print('-' * 70)

    tombs = bs_id.find_all('li', {'class': 'forecast-tombstone'})  # 타입 : <class 'bs4.element.ResultSet'>
    print('[find 함수 사용]')
    print('총 tombstone-container 검색 개수 :', len(tombs))
    print('-' * 70)

    for tomb in tombs:  # t의 타입 : <class 'bs4.element.Tag'>
        # print(tomb)
        pname = tomb.find('p', {'class':'period-name'})
        print('[Period]:', pname.text.strip() if pname else '')  # p의 속성이 period-name인 태그의 내용 추출

        short_desc = tomb.find('p', {'class': 'short-desc'})
        print('[Short desc]:', short_desc.get_text() if short_desc else '')

        temp = tomb.find('p', {'class': 'temp'})    # 'class': 'temp temp-low', 'temp temp-high' 둘 다 검색됨
        print('[Temperature]:', temp.get_text() if temp else '')

        img = tomb.find('img')
        print('[Image desc]:', img['title'] if img else '')  # <img> 의 title 속성 추출

        print('-' * 70)


def scraping_use_select(soup):
    bs_id = soup.select_one('ul#seven-day-forecast-list')       # 목표 코드에 가장 가까운 id
    print('National Weather Service Scraping')
    print('-' * 70)

    tombs = bs_id.select('li.forecast-tombstone')
    print('[select 함수 사용]')
    print('총 tombstone-container 검색 개수 :', len(tombs))
    print('-' * 70)

    for tomb in tombs:
        pname = tomb.select_one('p.period-name')
        print('[Period]:', pname.text if pname else '')

        short_desc = tomb.select_one('p.short-desc')
        print('[Short desc]:', short_desc.text if short_desc else '')

        # 만약, 클래스명 'temp temp-low'를 특정하고 싶다면 tomb.select_one('p.temp.temp-low') 를 사용하면 된다.
        # 클래스이름에 공백이 있는 경우, 그 공백을 '.'으로 대체하면 되기 때문.
        temp = tomb.select_one('p.temp')    # 'class': 'temp temp-low', 'temp temp-high' 둘 다 검색됨
        print('[Temperature]:', temp.text if temp else '')

        img = tomb.select_one('img')
        print('[Image desc]:', img['title'] if img else '')

        print('-' * 70)


url = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168'
html = urlopen(url)     # 그 url에 해당하는 html 저장
soup = BeautifulSoup(html, 'html.parser')  # 타입 : <class 'bs4.BeautifulSoup'>

scraping_use_find(soup)
scraping_use_select(soup)
