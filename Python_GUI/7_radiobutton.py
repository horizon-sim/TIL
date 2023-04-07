from tkinter import *

root = Tk()
root.title("자동화 프로그램")
# root.geometry("600x480") # 가로 * 세로
root.geometry("640x480+500+200") # 가로 *세로+ x좌표 + y좌표

Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar() # 여기에 int 형으로 값을 저장한다.
btn_burger1 = Radiobutton(root, text="햄버거0", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="햄버거1", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="햄버거2", value=3, variable=burger_var)
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요").pack()
drink_var = StringVar() # 값이 한글이니깐
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select() # 기본값 선택
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) # 햄버거 중 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get()) # 음료값 출력
btn = Button(root, text="주문", command=btncmd)
btn.pack()


root.mainloop() #창이 닫힐수있기때문에 계속 유지하기위해써준다.
