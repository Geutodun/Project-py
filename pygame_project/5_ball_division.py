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

#캐릭터 이동방향
character_to_x = 0

#캐릭터 속도
character_speed = 5

#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기 한번에 발사
weapons = []


#무기 이동 속도
weapon_speed = 10 


#공만들기 (4개 크기에 대해 따로 처리)
ball_images = [ 
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png")),
]

#공 크기에 따른 최초 이동 속도
ball_speed_y= [-18, -15, -12, -9] #index 0,1,2,3에 해당

#공들
balls = []

#최초 발생하는 큰공 추가
balls.append({
    "pos_x" : 50, #공의 x좌표
    "pos_y" : 50, #공의 y좌표
    "img_idx" : 0, #공의 이미지 인뎃스
    "to_x": 3, #x축 이동 방향(+ 오른쪽, - 왼쪽) 
    "to_y": -6, #t축 이동 방향
    "init_spd_y" : ball_speed_y[0] #y 최초 속도
    })

#사라질 무기, 공 정보 저장
weapon_to_remove = -1
ball_to_remove = -1


#이벤트 루프
running = True #게임이 진행중?
while running:
    dt = clock.tick(60)  #게임의 프레임 정하기

    #2이벤트 처리
    for event in pygame.event.get():  #어떤 사건 발생?
        if event.type == pygame.QUIT: #게임을 나가는 사건 발생?
            running = False   #게임 진행X
         
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로 이동
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: #캐릭터 오른쪽으로 이동
                character_to_x += character_speed                
            elif event.key == pygame.K_SPACE: #무기발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0       


    #3 게임 개릭터 위치 정의 
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
 
    #무기 위치 조정
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]  #무기 위치를 위로
    
    #천장에 닿은 무기 없애기
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0] #천장에 닿으면 사라짐

    #공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

    #가로벽에 닿았을 때 공 이동 위치 변경
    if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
        ball_val["to_x"] = ball_val["to_x"] * -1        

    #세로 위치
    #스테이지에 튕겨서 올라가는 처리
    if ball_pos_y >= screen_height - stage_height - ball_height:
        ball_val["to_y"] = ball_val["init_spd_y"]  
    else:  #그외츼 모든 경우에는 속도를 증가
        ball_val["to_y"] += 0.5     

    ball_val["pos_x"] += ball_val["to_x"]
    ball_val["pos_y"] += ball_val["to_y"]

    #4충돌처리
    

    #캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        #공 rect 정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        #공과 캐릭터 충돌 처리
        if character_rect.colliderect(ball_rect):
            running = False
            break
    
        #공과 무기들 충동처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            #무기 rect 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            #충돌 체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx #해당 무기 없애기 위한 설정
                ball_to_remove = ball_idx #해당 공 없애기 위한  값 설정
                
                #가장 작은 공이 아님면 한단계 작은 공으로 나누어짐
                if ball_img_idx < 3:

                    #현재 공 크기 정보
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    #나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    #왼쪽으로 팅겨 나가는 작은 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), #공의 x좌표
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), #공의 y좌표
                        "img_idx" : ball_img_idx + 1, #공의 이미지 인뎃스
                        "to_x": -3, #x축 이동 방향(+ 오른쪽, - 왼쪽) 
                        "to_y": -6, #t축 이동 방향
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1] #y 최초 속도
                    })

                    #오른쪽으로 튕겨 나가는 작은 공 
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), #공의 x좌표
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), #공의 y좌표
                        "img_idx"  : ball_img_idx + 1, #공의 이미지 인뎃스
                        "to_x": +3, #x축 이동 방향(+ 오른쪽, - 왼쪽) 
                        "to_y": -6, #t축 이동 방향
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1] #y 최초 속도
                    })
                break
         
    #충돌된 공, 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1


    #5 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
    
    
    pygame.display.update()  #게임화면 다시 그리기        



#게임 종료
pygame.quit()