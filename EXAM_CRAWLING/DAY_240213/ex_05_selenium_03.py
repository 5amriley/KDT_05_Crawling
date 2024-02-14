'''
    Selenium 사용 #3
    send_keys
    네이버 로그인
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

# User Agent 정보 추가
agent_option = webdriver.ChromeOptions()
user_agent_string = 'Mozilla/5.0'
agent_option.add_argument('user-agent=' + user_agent_string)

driver = webdriver.Chrome(options=agent_option)
driver.get('https://nid.naver.com/nidlogin.login')
driver.implicitly_wait(5)

# <input> 의 이름인 id를 검색
# <input> 태그와 같이 입력이 가능한 element는 send_keys() 함수로 키 입력 가능
driver.find_element(By.NAME, 'id').send_keys('실제_아이디')
driver.find_element(By.NAME, 'pw').send_keys('실제_패스워드')

# //*[@id="log.login"]
# driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
driver.find_element(By.ID, 'log.login').click()

driver.quit()
