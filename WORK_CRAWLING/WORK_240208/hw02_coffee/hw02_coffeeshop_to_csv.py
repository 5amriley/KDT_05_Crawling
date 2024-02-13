'''
    2024/02/12
    할리스 커피 매장 정보 스크레이핑 (scraping)
    - 지역, 매장명, 매장 주소, 전화번호
    - 수집된 정보는 csv 파일로 저장
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

# html 타입                        : <class 'http.client.HTTPResponse'>
# html.read() 타입                 : <class 'bytes'>
# html.read().decode('utf-8') 타입 : <class 'str'>
# soup 타입                        : <class 'bs4.BeautifulSoup'>
# id_contents 타입 (select_one)    : <class 'bs4.element.Tag'>
# tr_set 타입      (select)        : <class 'bs4.element.ResultSet'>
# tr_set[0] 타입                   : <class 'bs4.element.Tag'>
region_list, store_name, store_address, store_tel = [], [], [], []
count = 0

for i in range(1, 52):
    page_num = i  # 1 ~ 51
    html = urlopen(f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page_num}&sido=&gugun=&store=')
    soup = BeautifulSoup(html, 'html.parser')
    id_contents = soup.select_one('#contents')

    tr_set = id_contents.select('div.tableType01 > table > tbody > tr')

    for tr in tr_set:
        count += 1
        td_set = tr.select('td')
        region_list.append(td_set[0].text)  # 매장 지역
        store_name.append(td_set[1].text)  # 매장 이름
        store_address.append(td_set[3].text)  # 매장 주소
        store_tel.append(td_set[5].text)  # 매장 전화번호
        print(f'[{count:3d}] 지역: {td_set[0].text}, 매장이름: {td_set[1].text}, \
                                주소: {td_set[3].text}, 전화번호: {td_set[5].text}')

print(f'전체 매장 수: {count}')

# 데이터프레임 생성
hollysDF = pd.DataFrame({'지역':region_list, '매장명':store_name, '주소':store_address, '전화번호':store_tel})

# 데이터프레임 csv 파일로 저장
filename = 'hollys_branches.csv'
hollysDF.to_csv(filename, encoding='utf-8', index=False)
print(f'{filename} 파일 저장 완료')
