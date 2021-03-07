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

#스프라이트(캐릭터) 불러오기
character = pygame.image.load("E:\\파이썬\pygame_basic\\character.png")
character_size = character.get_rect().size   #이미지 크기 구함
cgaracter_width = character_size[0]  #캐릭터의 가로 크기
cgaracter_height = character_size[1]  #캐릭터의 세로 크기
cgaracter_x_pos = (screen_width / 2) - (cgaracter_width / 2)  #화면 가로 크기 절반에 위치 (가로)
cgaracter_y_pos = screen_height - cgaracter_height#화면 세로크기 가장 아래에 위치 (세로)




#이벤트 루프
running = True #게임이 진행중?
while running:
    for event in pygame.event.get():  #어떤 사건 발생?
        if event.type == pygame.QUIT: #게임을 나가는 사건 발생?
            running = False   #게임 진행X
    
    #screen.fill((0, 0, 255))     #R,G,B설정으로 스크린 채우기(fill:채우다)
    screen.blit(background, (0, 0))   #배경 그리기
    
    screen.blit(character, (cgaracter_x_pos, cgaracter_y_pos)) #캐릭터 그리기

    pygame.display.update()  #게임화면 다시 그리기



#게임 종료
pygame.quit()