import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창(VScode)
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기 정보(width, height)
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표정보
# pyautogui.click(fw.left + 30, fw.top+20)

# for w in pyautogui.getAllWindows():
    # print(w) # 모든 윈도우 가져오기

w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 윈도우 제목없으로된 첫번쨰값 가져오기
print(w)
# w.activate() # 활성화
if w.isActive == False: # 현재 활성화가 되지 않았다면
    w.activate()

if w.isMaximized == False: # 현재 최대화가 되지 않았다면
    w.maximize()

# if w.isMinimized == False: # 현재 최대화가 되지 않았다면
#     w.minimize()

pyautogui.sleep(1)
w.restore()

w.close() # 윈도우 닫기