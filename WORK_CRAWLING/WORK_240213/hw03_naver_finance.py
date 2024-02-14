'''
   2024/02/13 과제
   네이버 증시 정보 크롤링

   [풀이 핵심]
   1. selenium 으로 url 열어서 page_source 얻어내기 (html)
   2. 그 html 소스코드를 넘겨줘서 만든 BeautifulSoup 객체로 탐색하기
   3. 내가 원하는 자료가 어디에 있는지 코드에서 직접 찾아서 저장하기
'''

from bs4 import BeautifulSoup
from selenium import webdriver

TOP_N = 10  # 시가 총액 상위 TOP_N개

base = 'https://finance.naver.com'

driver = webdriver.Chrome()
driver.get('https://finance.naver.com/sise/sise_market_sum.naver')
driver.implicitly_wait(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

id_contentarea = soup.select_one('#contentarea')
tr_set = id_contentarea.select('div.box_type_l > table.type_2 > tbody > tr')

print('# 크롤링 시작 #')
href_list = []
company_name, company_code, cost_now, cost_ytd, cost_start, cost_high, cost_low = \
    [], [], [], [], [], [], []
cnt = 0
for tr in tr_set:
    # attrs <class 'dict'> : 각 tr 태그가 갖고 있는 속성 목록
    if 'onmouseover' in tr.attrs:
        td = tr.select('td')[1]
        a = td.select_one('a')
        href_list.append(a['href'])

        # selenium 으로 url 열어서 html 가져오면 <dl class="blind"> 획득 가능
        url2 = base + a['href']
        driver2 = webdriver.Chrome()
        driver2.get(url2)
        soup2 = BeautifulSoup(driver2.page_source, 'html.parser')
        blind = soup2.select_one('dl.blind')
        dd_set = blind.select('dd')
        # print(blind)
        company_name.append(dd_set[1].text.split()[1])  # 종목명
        company_code.append(dd_set[2].text.split()[1])  # 종목코드
        cost_now.append(dd_set[3].text.split()[1])      # 현재가
        cost_ytd.append(dd_set[4].text.split()[1])      # 전일가
        cost_start.append(dd_set[5].text.split()[1])    # 시가
        cost_high.append(dd_set[6].text.split()[1])     # 고가
        cost_low.append(dd_set[8].text.split()[1])      # 저가

        print(f'[{cnt+1:2}] {company_name[cnt]}')

        driver2.close()     # 창 닫기
        driver2.quit()      # webdriver 전체 종료

        cnt += 1
        if cnt >= TOP_N: break
driver.close()
driver.quit()
print('# 크롤링 종료 #')

while True:
    print('-' * 37)
    print(f'[ 네이버 코스피 상위 {TOP_N}대 기업 목록 ]')
    for i, v in enumerate(company_name):
        print(f'[{i + 1:2}] {v}')
    print('-' * 37)
    menu = input('주가를 검색할 기업의 번호를 입력하세요(-1: 종료): ')
    if menu == '-1':
        print('프로그램 종료')
        break
    if menu.isdecimal() and 0 < int(menu) <= TOP_N:
        print(href_list[int(menu) - 1])
        print(f'종목명: {company_name[int(menu) - 1]}')
        print(f'종목코드: {company_code[int(menu) - 1]}')
        print(f'현재가: {cost_now[int(menu) - 1]}')
        print(f'전일가: {cost_ytd[int(menu) - 1]}')
        print(f'시가: {cost_start[int(menu) - 1]}')
        print(f'고가: {cost_high[int(menu) - 1]}')
        print(f'저가: {cost_low[int(menu) - 1]}')
