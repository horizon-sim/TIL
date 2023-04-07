from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

browser.switch_to.frame('iframeResult')

# # cars 에 해당하는 element 를 찾고,내부에 있는 4번째 옵션을 선택
# elem = browser.find_elements_by_xpath('//*[@id="cars"]/option[3]')
# # option[1] 1번째 항목
# # option[2] 2번째 항목
# elem[0].click


# # 완전히 일치하는 텍스트 값을 통해서 선택하는 방법

# # 옵션 중에서 텍스트가 audi 인 항목을 선택
time.sleep(2)
# elem = browser.find_elements_by_xpath('//*[@id="cars"]/option[text()="Audi"]')
# elem[0].click()

# 텍스트 값이 부분 일치하는 항목 선택하는 방법
elem = browser.find_elements_by_xpath('//*[@id="cars"]/option[contains(text(), "Au")]')
elem[0].click()

time.sleep(5)
browser.quit()