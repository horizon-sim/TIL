from selenium import webdriver
import time

browser = webdriver.Chrome()
# browser.maximize_window() # 창 최대화

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult') # 프레임으로 전환

elem = browser.find_element_by_xpath('//*[@id="male"]')

# 선택이 안되어 있으면 선택하기
if elem.is_selected() == False: # 라디오 버튼이 선택되어 있지 않으면
    print("선택 안되어 있으므로 선택하기")
    elem.click()
else:
    print("선택 되어 있으므로 아무것도 안함")

time.sleep(3)

if elem.is_selected() == False: # 라디오 버튼이 선택되어 있지 않으면
    print("선택 안되어 있으므로 선택하기")
    elem.click()
else:
    print("선택 되어 있으므로 아무것도 안함")

browser.quit()