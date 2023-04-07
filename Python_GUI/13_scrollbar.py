from tkinter import *

root = Tk()
root.title("자동화 프로그램")
root.geometry("640x480+500+200")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")


# set 이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i) + "일") # 1일, 2일, ...
listbox.pack(side="left")

# 스크롤바를 움직여도 리스트박스가 움직이게 서로를 매핑
scrollbar.config(command=listbox.yview)

root.mainloop() 

