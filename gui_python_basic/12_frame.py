from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

Label(root, text="둘중 흥미 있는 분야는").pack(side="top")

Button(root, text="선택하기").pack(side="bottom")

#게임 프레임
frame_game = Frame(root, relief="solid", bd=1)
frame_game.pack(side="left", fill="both", expand=True)

Button(frame_game, text="FPS").pack()
Button(frame_game, text="RPG").pack()
Button(frame_game, text="Racing").pack()


#음악 프레임
frame_music = LabelFrame(root, text="음료")
frame_music.pack(side="right", fill="both", expand=True)
Button(frame_music, text="pop").pack()
Button(frame_music, text="k-pop").pack()


root.mainloop()