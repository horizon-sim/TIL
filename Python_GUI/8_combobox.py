import tkinter.ttk as ttk # 다른거 임포트 해야한다
from tkinter import *

root = Tk()
root.title("자동화 프로그램")
# root.geometry("600x480") # 가로 * 세로
root.geometry("640x480+500+200") # 가로 *세로+ x좌표 + y좌표

values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values,)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=5, values=values, state="readonly")
# state에 readonly 를 넣으면 적는게 불가능해지고 선택만가능
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()


root.mainloop() #창이 닫힐수있기때문에 계속 유지하기위해써준다.
