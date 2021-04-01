from random import *
e = randrange(1, 11)
x = 1

while x != e:
    x = int(input("값을 적어보세요:"))
    if x > e:
        print("작은 수 입니다.")
    elif x < e:
        print("더 큰 수 입니다.")
    elif x == e:
        print("정답입니다.")
