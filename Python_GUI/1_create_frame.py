from tkinter import *

root = Tk()
root.title("자동화 프로그램")
# root.geometry("600x480") # 가로 * 세로
root.geometry("640x480+500+200") # 가로 *세로+ x좌표 + y좌표

root.resizable(False, False) # x,y 값 변경 불가 (창 크기 변경 불가)

root.mainloop() #창이 닫힐수있기때문에 계속 유지하기위해써준다.
