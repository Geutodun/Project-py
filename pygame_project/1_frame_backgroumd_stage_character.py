import os
import pygame
#--------------------------------------------------------------
#기본 초기화 (반드시 해야함)


pygame.init()

#화면 크기
screen_width = 640  #가로
screen_height = 480  #세로
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀 설정
pygame.display.set_caption("Geutodun Pang") #게임이름   


#FPS
clock = pygame.time.Clock()


#--------------------------------------------------
#1.사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 폰트, 속도)

current_path = os.path.dirname(__file__) #현재 파일 위치 반환
image_path = os.path.join(current_path, "images") #images 폴터 위치 반환

#배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지의 높이 위에 캐릭터를 두기위해 사용

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height


#이벤트 루프
running = True #게임이 진행중?
while running:
    dt = clock.tick(60)  #게임의 프레임 정하기

    
    for event in pygame.event.get():  #어떤 사건 발생?
        if event.type == pygame.QUIT: #게임을 나가는 사건 발생?
            running = False   #게임 진행X
         
        

    #3 게임 개릭터 위치 정의 






    #4충돌처리
    

    

    #5 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()  #게임화면 다시 그리기




#게임 종료
pygame.quit()