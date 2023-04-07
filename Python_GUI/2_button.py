from tkinter import *

root = Tk()
root.title("자동화 프로그램")
root.geometry("640x480+500+200") # 가로 *세로+ x좌표 + y좌표

btn1 = Button(root, text="버튼1")
btn1.pack() # 우리눈에 버튼이 보이기위한 코드

btn2 = Button(root, padx=5, pady=10, text="버튼2") # 글자수에따르게 늘어난다.
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # 고정값
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="Python_GUI/image.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었습니다.")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop() #창이 닫힐수있기때문에 계속 유지하기위해써준다.
