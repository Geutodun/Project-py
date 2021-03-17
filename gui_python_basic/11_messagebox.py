import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# 기차 예매 시스템
def info():
    msgbox.showinfo("알림", "정상적으로 예매 되었습니다")

def warn():
    msgbox.showwarning("매진", "해당 좌석은 매진 되었습니다")    

def error():
    msgbox.showerror("오류", "오류가 발생 했습니다")  
    
def okcancel():
    msgbox.askokcancel("취소 / 확인", "해당 좌석은 커플 좌석입니다. 예매 하시겠습니까?") 

def retrycancel():
    response = msgbox.askretrycancel("다시 시도", "오류로 정상 처리 되지 않았습니다. 다시 시도 하시겠습니까?")      
    print("응답:", response) # 결과 True, False -> 예 1, 아니요 0
    
    if response == 1: #재시도
        print("전 페이지로 돌아갑니다")
    elif response == 0: # 취소
        print("메인페이지로 돌아갑니다")



def yesno():
    msgbox.askyesno("예 / 아니요", "해당 좌석은 2인이상만 예매 가능합니다. 예매 하시겟습니까")      

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="일정 시간 입력이 없어서 자동으로 로그아웃 되었습니다. \n 다시 로그인 하시겟습니까? 취소를 누르면 페이지에서 나가짐니다.")  

    print("응답:", response) # 결과 True, False, None -> 예 1, 아니요 0, 그 외
    
    if response == 1: #네
        print("로그인 화면으로 넘어갑니다.")
    elif response == 0: #아니요
        print("메인페이지로 돌아갑니다.")
    else:
        print("페이지에서 나갑니다.")
    



Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="매진").pack()
Button(root, command=error, text="오류").pack()

Button(root, command=okcancel, text="취소 확인").pack()
Button(root, command=retrycancel, text="다시 시도").pack()
Button(root, command=yesno, text="예 아니요").pack()
Button(root, command=yesnocancel, text="예 아니요 취소").pack()


root.mainloop()