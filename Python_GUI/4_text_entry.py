from tkinter import *

root = Tk()
root.title("자동화 프로그램")
# root.geometry("600x480") # 가로 * 세로
root.geometry("640x480+500+200") # 가로 *세로+ x좌표 + y좌표

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) # enter가 안되기때문에 ex) 아이디적는칸
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 처음부터 끝까지 모든텍스트를 가져오는뜻
    #  앞에 1은 line 1, 0은 coulum기준 0번째부터
    print(e.get()) # entry는 e.get만 있으면 됩니다.

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()



root.mainloop() #창이 닫힐수있기때문에 계속 유지하기위해써준다.
