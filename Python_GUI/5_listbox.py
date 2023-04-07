from tkinter import *

root = Tk()
root.title("자동화 프로그램")
# root.geometry("600x480") # 가로 * 세로
root.geometry("640x480+500+200") # 가로 *세로+ x좌표 + y좌표

listbox = Listbox(root, selectmode="extended", height=0) # selectmode 중에 single로하면 하나밖에 선택못함
# height는 화면에 보이는 숫자 0으로 적으면 모든 리스트를 다보여줌
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(END) # 맨 뒤에 항목을 삭제
    # listbox.delete(0) # 맨 앞에 항목을 삭제

    # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인 (시작 idx, 끝 idx)
    # print("1번째부터 3번째가의 항목 : ", listbox.get(0,2))

    # 선택된 항목 확인 (위치로 반환 )
    print("선택된 항목 : ", listbox.curselection())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()



root.mainloop() #창이 닫힐수있기때문에 계속 유지하기위해써준다.
