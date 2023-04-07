import time
import tkinter.ttk as ttk # 콤보박스,프로그레스 ttk 필요함
from tkinter import *

root = Tk()
root.title("자동화 프로그램")
# root.geometry("600x480") # 가로 * 세로
root.geometry("640x480+500+200") # 가로 *세로+ x좌표 + y좌표

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# indeterminate는 언제끝날지 모르는작업 표시 유용
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(5) # 5 ms 마다 움직임
# progressbar.pack()


# def btncmd():
#     progressbar.stop() # 작동 중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

# 실전 프로그레스 바 예시

p_var2 = DoubleVar() # 1.5 ~ 뭐이런식으로 올라갈수도있어서
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.01) # 0.01 초 대기

        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() # UI 업데이트
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop() #창이 닫힐수있기때문에 계속 유지하기위해써준다.
