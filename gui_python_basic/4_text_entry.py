from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)   #여러줄로 입력할때
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)  #한줄로 입력 할떄
e.pack()
e.insert(0, "한줄만 입력")

def btncmd():  #내용을 터미널에 입력
    print(txt.get("1.0", END)) #1 : 첫번째 라인, 0 : 0번째 colum 위치
    print(e.get())

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()