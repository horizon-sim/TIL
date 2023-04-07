import pyautogui
import pyperclip
import sys
######################## 내가 직접만든 코드 #################

# pyautogui.sleep(3) # 3초 대기 , 내 마우스 위치를 알기위해서
# print(pyautogui.position())

# pyautogui.hotkey("winleft", "r")
# pyautogui.sleep(0.5)
# pyautogui.write("mspaint")
# pyautogui.sleep(0.5)
# pyautogui.press("enter")
# pyautogui.sleep(0.5)
# text_btn = pyautogui.locateOnScreen("text.png", confidence=0.8)
# pyautogui.sleep(0.2)
# pyautogui.click(text_btn)
# pyautogui.sleep(0.5)
# pyautogui.click(x=219, y=295, duration=0.05)
# pyautogui.sleep(0.5)
# pyperclip.copy("참 잘했어요")
# pyautogui.hotkey("ctrl", "v")
# x_btn = pyautogui.locateOnScreen("x.png", confidence=0.8)
# pyautogui.sleep(0.2)
# pyautogui.click(x_btn)
# pyautogui.sleep(0.5)
# save_btn = pyautogui.locateOnScreen("not_save.png", confidence=0.8)
# pyautogui.sleep(0.2)
# pyautogui.click(save_btn)

#############################################################
##################### 나도코딩 코드 ##########################

pyautogui.hotkey("win", "r")
pyautogui.write("mspaint") # 프로그램 명 입력
pyautogui.press("enter") # 엔터 키 입력

# 그림판 나타날 떄까지 2초 대기
pyautogui.sleep(1)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0] # 그림판 1개만 띄워져 있다고 가정
if window.isMaximized ==  False:
    window.maximize() # 최대화

btn_text = pyautogui.locateOnScreen("text.png")
if btn_text:
    pyautogui.click(btn_text, duration=0.5)
else:
    print("찾기 실패")
    sys.exit()

# 흰 영역 클릭
pyautogui.click(200, 200, duration=0.5)

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("참 잘했어요")

# 5초 대기
pyautogui.sleep(5)

# 프로그램 종료
window.close()
pyautogui.sleep(0.5)
pyautogui.press("n") # 저장하지 않음


##################번외#####################

btn_text1 = pyautogui.locateOnScreen("text.png")
pyautogui.click(btn_text.left - 200, btn_text.top + 200) # 상대좌표로 하는것도된다