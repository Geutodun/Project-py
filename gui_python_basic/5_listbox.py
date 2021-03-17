from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")
                                    #선택할수있는 글자의 개수
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")                         #리스트에 들어있는 내용중 지정된 갯수만 보여줌(0은 다보여줌)
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")  #end는 글자를 마지막에 가게함
listbox.pack()

def btncmd():  
    #삭제
    #listbox.delete(0) #맨앞내용 삭제
    #listbox.delete(END) #맨뒤 내용 삭제

    #갯수 확인 
    #print("리스트에는", listbox.size(), "개가 남아 있습니다")

    #항목 확인 (시작 내용[idx], 끝 내용[idx])
    #print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    #선택된 항목 확인 (idx로 출력) (위치로 출력 ex:1, 2, 3)
    print("선택된 항목 : ", listbox.curselection())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()