from tkinter import *

root = Tk()
root.title("자동화 프로그램")
root.geometry("640x480+500+200")

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0) # root에 넣는게아니라 menu에 넣는다.
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator() # 구분자
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) # 프로그램 종료

menu.add_cascade(label="File", menu=menu_file) # 메뉴에 넣기

# Edit 메뉴 (빈 값)
menu.add_cascade(label="Edit")

# Language 메뉴 추가 (radio 버튼을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="language", menu=menu_lang)

# View 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu) # root에 포함하려면 이걸 넣어야한다.
root.mainloop() 
