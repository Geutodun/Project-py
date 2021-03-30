print("정사각형 넓이 구하기") 
x = int(input("정사각형 변의 길이:"))
y = x ** 2 
print("정사각형 넓이:{}".format(y))


print("직사각형 넓이 구하기")
e = int(input("직사각형 가로의 길이:"))
z = int(input("직사각형 세로의 길이:"))
r = e * z
print("직사각형의 넓이:{}".format(r))

print("사다리꼴 넓이 구하기")
j = int(input("사다리꼴 높이 길이:"))
k = int(input("사다리꼴 윗변의 길이:"))
l = int(input("사다리꼴 아랫변의 길이:"))
g = j * (k + l) / 2
print("사다리꼴 넓이:{}".format(g))
