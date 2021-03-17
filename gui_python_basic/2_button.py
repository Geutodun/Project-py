from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")  #공간 확보후 설정 됨(글이 많으면 그에 맞게 공간 설정)
btn2.pack()        #가로크기  #세로 크기

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4")  #버튼 크기 자체를 설정 (글이 많아도 제한된 공간이라 글이 짤림)
btn4.pack()

btn5 = Button(root, fg="red", bg="blue", text="버튼5")
btn5.pack()        #글자색깔    #배경색        

photo = PhotoImage(file="gui_python/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작 버튼", command=btncmd)  #버튼이 동작되게 해보기
btn7.pack()

root.mainloop()