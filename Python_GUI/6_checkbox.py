from tkinter import *

root = Tk()
root.title("자동화 프로그램")
# root.geometry("600x480") # 가로 * 세로
root.geometry("640x480+500+200") # 가로 *세로+ x좌표 + y좌표

chkvar = IntVar() # chkvar 에 int 형으로 값을 저장한다.
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# 체크박스에는 variable은 체크박스를 체크했을때의 값을 가져올수있다.
chkbox.select() # 자동 선택 처리
chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
   print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
   print(chkvar2.get()) 
   

btn = Button(root, text="클릭", command=btncmd)
btn.pack()



root.mainloop() #창이 닫힐수있기때문에 계속 유지하기위해써준다.
