from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.get('https://flight.naver.com/flights/')
browser.maximize_window()

# 가는 날 클릭
go_btn = browser.find_element_by_link_text('가는날 선택')
time.sleep(0.5)
go_btn.click()

# 여러개 이므로 elements 츠로한다. 엘리먼트말고 엘리먼츠
go_day = browser.find_elements_by_link_text('28')[0]
time.sleep(0.5)
go_day.click()

# 오는 날 클릭
back_day = browser.find_elements_by_link_text('29')[0]
time.sleep(0.5)
back_day.click()

# 제주도 클릭
place = browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]/div/span')
time.sleep(0.5)
place.click()

# 항공권 검색
search = browser.find_element_by_link_text('항공권 검색')
time.sleep(0.5)
search.click()


# 첫번째 단순한방법 : 시간낭비
# time.sleep(10)

# 두번쨰 기다리는방법 : 로딩이필요할경우 이코드 쓰자 ㅋ~
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    print(elem.text)
except:
    print("실패했어요")

# 첫번째 결과 출력
# elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
# print(elem.text) # element 내에 있는 text 부분을 출력


time.sleep(5)
browser.quit()


# # 월만 다르고 같은 날짜일땐 이런식으로 한다. 클릭하면 element가 바뀌기때문
# go_day = browser.find_elements_by_link_text('30')[0]
# time.sleep(0.5)
# go_day.click()

# # 오는 날 클릭
# back_day = browser.find_elements_by_link_text('30')[0]
# time.sleep(0.5)
# back_day.click()

