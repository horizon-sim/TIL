# from PIL.ImageOps import grayscale
import pyautogui
file_menu = pyautogui.locateOnScreen("file_menu.png")
print(file_menu)

# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 이미지가 없는경우

# screenshot = pyautogui.locateOnScreen("screenshot.png")
# print(screenshot)
# pyautogui.moveTo(screenshot)

# 똑같이생긴거 여러개 클릭 가능
# for i in pyautogui.locateAllOnScreen("text_n.png"):
#     print(i)
#     pyautogui.moveTo(i)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 속도 개선
# 1. GrayScale
# 정확도 좀 떨어짐
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True) # 이미지를 흑백으로 전환하면서 함
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정
# ㄹㅇ 엄청빠름
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1722, 757, 1899 - 1722, 839 - 757))
# pyautogui.moveTo(trash_icon)

# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen("run_button.png", confidence=0.9) # 90퍼 이상 일치하면
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")

# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견실패")
# pyautogui.click(file_menu_notepad)
# print("발견성공")

# 2. 일정 시간동안 기다리기 (timeout)
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time()
#     if end - start > timeout: # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit()

# pyautogui.click(file_menu_notepad)
def find_target(img_file, timeout):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout: # 지정한 10초를 초과하면
            break 
    return target


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}).")
        sys.exit()

# my_click("file_menu_notepad.png", 1)