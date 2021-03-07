import pygame

pygame.init()

#화면 크기
screen_width = 480  #가로
screen_height = 640  #세로
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀 설정
pygame.display.set_caption("Geutodun game") #게임이름   

#배경 이미지 불러오기
background = pygame.image.load("E:\\파이썬\pygame_basic\\background.png")


#이벤트 루프
running = True #게임이 진행중?
while running:
    for event in pygame.event.get():  #어떤 사건 발생?
        if event.type == pygame.QUIT: #게임을 나가는 사건 발생?
            running = False   #게임 진행X
    
    #screen.fill((0, 0, 255))     #R,G,B설정으로 스크린 채우기(fill:채우다)
    screen.blit(background, (0, 0))   #배경 그리기

    pygame.display.update()  #게임화면 다시 그리기



#게임 종료
pygame.quit()