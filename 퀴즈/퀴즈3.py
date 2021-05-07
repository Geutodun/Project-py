a = "http://naver.com"
x = a.replace("http://", "")
x = x[:x.index(".")] #.전까지 출력하라

passoward = x[:3] + str(len(x)) + str(x.count("e")) + "!"

print("{}의 생성된 비밀번호 : {}".format(a, passoward))
