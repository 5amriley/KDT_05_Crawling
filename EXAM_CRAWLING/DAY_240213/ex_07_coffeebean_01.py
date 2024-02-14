'''
    동적 웹페이지 크롤링 #1
    Coffee Bean 매장 찾기
'''

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.coffeebeankorea.com/store/store.asp')

# 팝업창 생성됨 ('삼성봉은사거리점')
driver.execute_script('storePop2(31)')   # execute_script(자바스크립트)

# 현재의 html 소스를 저장
html = driver.page_source   # page_source: 해당 웹페이지의 소스가 저장됨
soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())  # HTML 소스코드를 보기 좋게 출력 (출력량 엄청 많음)

store_names = soup.select('div.store_txt > p.name > span')
store_name_list = []
for name in store_names:
    store_name_list.append(name.get_text())

print('매장 개수: ', len(store_name_list))
print(store_name_list)

store_addresses = soup.select('p.address > span')
store_address_list = []
for addr in store_addresses:
    print(addr.get_text())
    store_address_list.append(addr.get_text())

# driver.quit()   # web driver 종료
