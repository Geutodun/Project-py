import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1 ,32)] #1에서 31까지의 숫자 
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()                  #목록이 5개까지 보여짐
combobox.set("카드 결제일") #최초 목록 제목 설정 + 버튼 클릭을 통한 값 설정도 가능
                                    #목록이 10개까지 보여짐
read_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") #읽기 전용 (안에 문자열을 넣을수 없음)
read_combobox.current(0) #0번째 값 선택
read_combobox.pack()

def btncmd():  
    print(combobox.get()) 
    print(read_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()