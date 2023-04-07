import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("asefasees", interval=0.1)
# pyautogui.write("sdfawse") # 영문하고 숫자만됨

# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter","1"], interval=0.3)
# 순서대로 나눠서 입력가능

# 특수 문자
# shift 4 -> $
# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# 조합키 (Hot key)

# Ctrl + A
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # press("a")
# pyautogui.keyUp("ctrl")

# 간편한 조합키
# pyautogui.hotkey("ctrl", "a", "alt", "shift")
# 순서대로 누르고누르고 눌렀다가 떼고 뗴고
# pyautogui.hotkey("ctrl", "a")

import pyperclip
# pyperclip.copy("안녕") # "안녕" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl", "v") # 클립보드에 있는 내용을 붙여넣기
def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


# win : ctrl + alt + del 누르면 자동화 끝