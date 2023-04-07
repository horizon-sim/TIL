import pyautogui

pyautogui.sleep(3) # 3초 대기 , 내 마우스 위치를 알기위해서
print(pyautogui.position())
x = pyautogui.position()

# pyautogui.click(x=955, y=15, duration=1) # 1초 동안 (955, 15) 좌표로 이동후 마우스 클릭
# pyautogui.click()
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=2) # 이것도 더블클릭

# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown() # 마우스 버튼 누른 상태
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp() # 마우스를 뗀 상태

# pyautogui.rightClick()
# pyautogui.middleClick() # 휠느낌

# pyautogui.moveTo(881, 213)
# # pyautogui.drag(200, 0, duration=0.25) # 상대 좌표, duration을 넣어주자~

# pyautogui.dragTo(1081, 213, duration=0.5) # 절대 좌표 기준으로 이동

# pyautogui.scroll(-800) # 위 방향으로 300만큼 스크롤(음수는 아래)

