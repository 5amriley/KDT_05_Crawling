'''
    chromedriver 자동 다운로드
'''

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://www.naver.com')
print(driver.current_url)

sleep(2)
driver.close()  # 하나의 탭만 종료
driver.quit()   # webdriver 전체 종료
