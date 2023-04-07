from tkinter import *

root = Tk()
root.title("자동화 프로그램")
# root.geometry("600x480") # 가로 * 세로
root.geometry("640x480+500+200") # 가로 *세로+ x좌표 + y좌표

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="Python_GUI/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="버튼 눌렀지?") # config는 무언가를 바꿔주는듯?
    
    global photo2 # 전역번수로 지정해야 함수가 끝나도 안사라진다.★★중요
    photo2 = PhotoImage(file="Python_GUI/image.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change) # 라벨1 바꾸기
btn.pack()

root.mainloop() #창이 닫힐수있기때문에 계속 유지하기위해써준다.