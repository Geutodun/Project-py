from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

#set
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set)

for i in range(1, 32): 
    listbox.insert(END, str(i) + "일") #1일 2일 3일 . . . . . 31일
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()