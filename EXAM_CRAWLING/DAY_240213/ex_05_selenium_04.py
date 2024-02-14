'''
    Selenium 사용 #4
    구글 검색어 입력
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://google.com')
#driver.implicitly_wait(3)

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Python')
search_box.submit()     # 검색 버튼 누름

time.sleep(3)

# CSS 셀렉터로 접근
search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
print(len(search_results))

# Extract and print the title and URL of each search result
for result in search_results:
    # 검색 결과에서 <h3> 태그값 가져옴
    title_element = result.find_element(By.CSS_SELECTOR, 'h3')
    title = title_element.text.strip()
    print(f'{title}')

driver.quit()
