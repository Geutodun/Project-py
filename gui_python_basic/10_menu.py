from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

def create_new_file():
    print("새로운 파일을 만듭니다")

menu = Menu(root)


#파일 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="새로운 파일", command=create_new_file)
menu_file.add_command(label="새 윈도우")
menu_file.add_separator()
menu_file.add_command(label="파일 열기....")
menu_file.add_separator()
menu_file.add_command(label="저장", state="disable") #비활성화
menu_file.add_separator()
menu_file.add_command(label="나가기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)


#에디트 메뉴
menu.add_cascade(label="에디트")

#언어 버튼 추가 (radio 버튼을 통해 언어를 선택 할수 있게)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="파이썬")
menu_lang.add_radiobutton(label="자바")
menu_lang.add_radiobutton(label="C")
menu.add_cascade(label="언어", menu=menu_lang)

# view 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="미니맵 보이기")
menu.add_cascade(label="View", menu=menu_view)


root.config(menu=menu)
root.mainloop()