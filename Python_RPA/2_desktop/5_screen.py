import pyautogui
# # 스크린 샷 찍기

# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()
# 983,18 47,163,241 #2FA3F1

pixel = pyautogui.pixel(983, 18)
print(pixel)

# print(pyautogui.pixelMatchesColor(983, 18, pixel))
# print(pyautogui.pixelMatchesColor(983, 18, (47, 163, 241)))
# print(pyautogui.pixelMatchesColor(983, 18, (48, 163, 241))) # 색이틀리면 False
