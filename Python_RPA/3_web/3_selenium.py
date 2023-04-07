from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# browser = webdriver.Chrome("./chromedriver.exe")

# 크롬 키는거
browser = webdriver.Chrome() 

# 그 크롬을 해당 링크로 이동
browser.get("http://naver.com")

# 해당(카페 라는 글자) 글자를 찾아서 반환
elem = browser.find_element_by_link_text("카페")

# 해당 글자가 포함된 코드 가져오기
elem.get_attribute("href")
elem.get_attribute("class")

# 클릭
elem.click()

# 뒤로가기
browser.back() 

# 앞으로 가기
browser.forward() 

# 새로고침
browser.refresh() 

# 예시
elem = browser.find_elements_by_id("query")
elem[0].send_keys("안녕하세요") # id는 [0] 붙여줘야하는거같음
elem[0].send_keys(Keys.ENTER)
elem = browser.find_element_by_tag_name("a") # 링크 가져오기
elems = browser.find_elements_by_tag_name("a") # 각각의 모든 a 태그가져오기

for e in elems:
    e.get_attribute("href") # 수많은 a 태그안에있는 링크를 다가져온다

# 예시 2
browser.get("http://daum.net")

elem = browser.find_element_by_name("q")
elem.send_keys("안녕하세요") # 이건 왜 [0] 이거 안붙지?

elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')
# 큰따옴표 헷갈릴수 있기에 작은따옴표로 앞뒤를 해줌으로써 오류를 배제 할수있다. (웹자동화 할떄는 ''이거 사용)
elem.click()

# 스크린샷
browser.save_screenshot('daum.png')

# 종료
browser.close() # 현재 탭만 닫기
browser.quit() # 전체 종료