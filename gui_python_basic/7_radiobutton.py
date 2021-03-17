from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar() #int형으로 저장
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="치킨햄버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="불고기햄버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요").pack()

drink_var = StringVar() #문자열로 저장
btn_drink1 = Radiobutton(root, text="제로콜라", value="제로콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="나랑드사이다", value="나랑드사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():  
    print(burger_var.get())    #선택된 값 출력
    print(drink_var.get()) #음료중 선택된 문자열 출력

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()