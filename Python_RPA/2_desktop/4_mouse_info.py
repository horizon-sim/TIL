import pyautogui
# pyautogui.FAILSAFE = False # 구석가면 취소되는 현상 취소하기 (추천안함)
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
# pyautogui.mouseInfo()

# pyautogui.moveTo(1016, 21)

for i in range(3):
    pyautogui.move(100, 100)