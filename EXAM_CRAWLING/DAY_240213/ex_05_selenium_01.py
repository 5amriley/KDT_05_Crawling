'''
    Selenium 사용 #1
'''

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.google.com')

print(driver.current_url)
print(driver.title)
print(driver.page_source)   # 전체 html

driver.implicitly_wait(time_to_wait=5)  # 검색하려는 요소가 로딩될 때까지 지정한 시간만큼 대기할 수 있도록 설정 (최대 5초)
driver.close()
driver.quit()
