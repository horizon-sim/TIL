
#################### 내가 만든 코드 ########################################
# from selenium import webdriver
# import time

# browser = webdriver.Chrome()
# browser.maximize_window()

# browser.get('https://www.w3schools.com')

# # 변수
# first_name = "나도"
# last_name = "코딩"
# # country = "Canada"
# subject = "퀴즈 완료하였습니다."


# learn_html_btn = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/a[1]')
# time.sleep(0.5)
# learn_html_btn.click()

# time.sleep(1.5)

# howto_btn = browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]')
# time.sleep(0.5)
# howto_btn.click()

# time.sleep(1.5)

# contact_btn = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]')
# time.sleep(0.5)
# contact_btn.click()

# time.sleep(1.5)

# first_name_input = browser.find_element_by_xpath('//*[@id="fname"]')
# time.sleep(0.5)
# first_name_input.send_keys(first_name)

# time.sleep(0.5)

# last_name_input = browser.find_element_by_xpath('//*[@id="lname"]')
# time.sleep(0.5)
# last_name_input.send_keys(last_name)

# time.sleep(0.5)

# elem_c = browser.find_elements_by_xpath('//*[@id="country"]/option[contains(text(), "Cana")]')
# time.sleep(0.5)
# elem_c[0].click()

# time.sleep(0.5)

# subject_input = browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea')
# time.sleep(0.5)
# subject_input.send_keys(subject)


# time.sleep(3)
# browser.quit()

###################################################################################

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()


# 1. https://www.w3schools.com 접속 (URL 은 구글에서 w3schools 검색)
browser.get('https://www.w3schools.com')

# 2. 화면 중간 LEARN HTML 클릭
browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/a[1]').click()
time.sleep(0.1)

# 3. 상단 메뉴 중 HOW TO 클릭
browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()
time.sleep(1)

# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭

# 4-1. 기본 (나중에 새로운 element가 추가될때 오류가능성 있음)
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]').click()

# 4-2. 텍스트 같은것 찾기 (Contact Form 이라는 텍스트가 2개이상이면 실패함)
# browser.find_element_by_link_text('Contact Form').click()

# 4-3. 어떤 태그 밑에 특정 텍스트 찾기 (가장 좋은방법)
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()

# 4-4. 일부 텍스트 비교
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]')

time.sleep(0.1)

# 5. 입력란에 아래 값 입력
first_name = "나도"
last_name = "코딩"
country = "Canada"
subject = "퀴즈 완료하였습니다."

browser.find_element_by_xpath('//*[@id="fname"]').send_keys(first_name)
browser.find_element_by_xpath('//*[@id="lname"]').send_keys(last_name)
browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(country)).click()
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(subject)

time.sleep(3)
browser.quit()