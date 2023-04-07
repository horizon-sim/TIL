import pyautogui

# 절대 좌표로 마우스 이동
# pyautogui.moveTo(100, 100) # 지정한 위치(가로 x, 세로 y)로 마우스를 이동
# pyautogui.moveTo(100, 200, duration=5) # 5 동안 100, 200 위치로 이동

pyautogui.moveTo(100, 100, duration=1)
# pyautogui.moveTo(200, 200, duration=1)
# pyautogui.moveTo(300, 300, duration=1)

# 상대 좌표로 이동 (현재 커서가 있는 위치로부터)
# pyautogui.moveTo(100, 100, duration=1)
# print(pyautogui.position()) # point(x, y)
# pyautogui.move(100, 100, duration=1) # 100, 100 기준으로 +100이니까 200, 200 이다.
# print(pyautogui.position()) # point(x, y)
# pyautogui.move(100, 100, duration=1) # 위와 같다
# print(pyautogui.position()) # point(x, y)

# p = pyautogui.position()
# print(p[0], p[1]) # x, y 좌표 값이 나옴
# print(p.x, p.y) # x, y

