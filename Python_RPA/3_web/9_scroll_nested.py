from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')
browser.maximize_window()

time.sleep(2)

# 특정 영역 스크롤
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[61]')
time.sleep(1)

# 방법 1 : ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()
# 가장아래에 보임

# 방법 2 : 좌표 정보 이용
xy = elem.location_once_scrolled_into_view # 함수가 아니니까 () 쓰지않음
print("type : ", type(xy)) # dict
print("value : ", xy)

time.sleep(1)
elem.click()

# 사실 스크롤은 특정 영역스크롤안해도 클릭은 가능


time.sleep(5)
browser.quit()