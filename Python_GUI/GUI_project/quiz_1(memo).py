import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480+500+200")


# 함수 영역

filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): # 파일 있으면 true, 없으면 false
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 본문 삭제
            txt.insert(END, file.read()) # 본문입력 ,위젯에 넣음 file.read()는 어떤내용을? 부분임

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장

# 메뉴 영역
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file) # command 뒤에는 ()붙이지 않기
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit) # 프로그램 종료

menu.add_cascade(label="파일(F)", menu=menu_file) # 메뉴에 넣기
menu.add_cascade(label="편집(E)")
menu.add_cascade(label="서식(O)")
menu.add_cascade(label="보기(V)")
menu.add_cascade(label="도움말(H)")

# 스크롤바 영역
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")


# 내용 영역
txt = Text(root, yscrollcommand=scrollbar.set) # 서로 매핑
txt.pack(side="left", fill="both", expand=True) # 꽉 채우는것
scrollbar.config(command=txt.yview) # 서로 매핑


root.config(menu=menu) # 메뉴 영역필수
root.mainloop() # 전체 영역필수

