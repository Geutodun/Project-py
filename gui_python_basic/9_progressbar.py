import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

#progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") #좌우로 움직임
#progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") #다운로드
#progressbar.start(10) #10초마다 움직임
#progressbar.pack()

#def btncmd():  
        #progressbar.stop() #멈춤

#def btncmd2():  
        #progressbar.start(30)

#btn = Button(root, text="중지", command=btncmd)
#btn.pack()

#btn2 = Button(root, text="다시 시작", command=btncmd2)
#btn2.pack()

p_var2 = DoubleVar()                                 #프로그래스바 길이
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd3():
    for i in range(1, 101): 
            time.sleep(0.01) #0.01초 대기

            p_var2.set(i)   #프로그래스바 값 설정
            progressbar2.update()  #ui 업데이트
            print(p_var2.get())

btn = Button(root, text="시작", command=btncmd3)
btn.pack()


root.mainloop()