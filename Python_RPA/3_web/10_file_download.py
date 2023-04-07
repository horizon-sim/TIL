from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'C:\코딩\python test'})

browser = webdriver.Chrome(options=chrome_options) # 다운로드 경로를 옵션으로 정함
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to.frame('iframeResult')

# download 링크 클릭
elem = browser.find_element_by_xpath('/html/body/p[2]/a')
time.sleep(1)
elem.click()



time.sleep(3)
browser.quit()