import pygame
from pygame import mixer

#pygame initionization
pygame.init()

#create game window
screen = pygame.display.set_mode((800,600))

#set game window icon

icon = pygame.image.load("img/planet.png")
pygame.display.set_icon(icon)

#set game caption
pygame.display.set_caption("Astro Hacker")

#background image
bgImg = pygame.image.load("img/galaxy.jpg")

#background music
mixer.music.load("sound/background.wav")
mixer.music.play(-1)

#game text fonts
scf = pygame.font.Font('freesansbold.ttf',32)
lf  = pygame.font.Font('freesansbold.ttf',32)
go  = pygame.font.Font('freesansbold.ttf',72)

#player score text
player_score = 0
def show_score():
    score = scf.render("Score : "+str(player_score), True, (255,255,255))
    screen.blit(score,(50,50))

#player life text
player_life = 100
def show_life():
    life = lf.render("Life :"+str(player_life),True,(255,255,255))
    screen.blit(life, (550,50))

#game over text
def game_over():
    gover = go.render("Game Over",True,(255,255,255))
    screen.blit(gover,(200,300))

#Player 
playerImg = pygame.image.load("img/player.png")

player_move_v = 0
player_move_h = 0
playerX = 380
playerY = 500

def player(x,y):
    screen.blit(playerImg,(x,y))


#Bullets
# bulletY = 0
bulletImg = pygame.image.load("img/bullet.png")
bulletX = 0
bulletY = 0
bullet_state = False

def bullet(x,y):
    screen.blit(bulletImg, (x,y))
    # global bullet_state
    # bullet_state = True 

#astroids
astroImg = pygame.image.load("img/ulka.png")
astro_x_list = [20,70,120,170,220,270,320,370,420,470,550,500,650,700,750]
astro_y_list = [550,200,50,200,100,450,80,190,500,250,120,450,30,380,200]

#astroids range
astro_ranges = []
astro_draw_access = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
def astro(x,y):
    screen.blit(astroImg,(x,y))






#game loop
loop_run = True

while loop_run:

    screen.blit(bgImg,(0,0))
    #color background
    # screen.fill((229, 250, 5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop_run = False
        
        #player Handle
        if event.type == pygame.KEYDOWN:
            #detect up arrow key
            if event.key == pygame.K_UP:
                print("UP")
                #player move change
                player_move_v = -5
            #detect down arrow key    
            if event.key == pygame.K_DOWN:
                print("DOWN")
                #player move change
                player_move_v = 5
            #detect left arrow key
            if event.key == pygame.K_LEFT:
                print("LEFT")
                #player move change
                player_move_h = -5
            #detect right arrow key
            if event.key == pygame.K_RIGHT:
                print("RIGHT")
                #player move change
                player_move_h = 5
            #Fire Bullets
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound("sound/shoot.wav")
                bullet_sound.play()
                bulletX = playerX + 20
                bulletY = playerY 
                bullet_state = True
                bullet(bulletX,bulletY)
                


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_move_v = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_move_h = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_btn = pygame.mouse.get_pressed()
            
            if mouse_btn[0]:
                bullet_sound = mixer.Sound("sound/shoot.wav")
                bullet_sound.play()
                bulletX = playerX + 20
                bulletY = playerY 
                bullet_state = True
                bullet(bulletX,bulletY)
                


    #player go to Vertical
    playerY += player_move_v  

    #player go to Horizontal Way
    playerX += player_move_h  

    # player limitation
    #------------- Y Limitation --------------
    if playerY <= 20:
        playerY = 20
    if playerY >= 520:
        playerY = 520
    #------------- X Limitation --------------
    if playerX <= 20:
        playerX = 20
    if playerX >= 720:
        playerX = 720
    
    #Call to player
    player(playerX,playerY)

    #bullet go to up
    if bullet_state == True:
        bulletY -= 5
        bullet(bulletX, bulletY)  

    #astroids
   
    for x in range(15):
        astro_y_list[x] += 0.5
        if astro_draw_access[x] == 1:
            astro(astro_x_list[x],astro_y_list[x])

        #astroid draw again limitation
        if astro_y_list[x] >= 600:
            astro_y_list[x] = -30

        #atroids x rangeadd to list
        astro_ranges.append(range(astro_x_list[x]-5,astro_x_list[x]+44))

        #increase player score
        if bulletX in astro_ranges[x]:
            if bulletY <= astro_y_list[x]+64:
                astro_draw_access[x] = 0 
                astro_ranges [x] = range(-20,-40)
                player_score += 10
                print(astro_x_list[x])

        #decrease player Life
        if astro_y_list[x] >= 599.5:
            player_life -= 10 
        
        #game over
        if player_life <= 0:
            player_life = 0
            for a in range(15):
                astro_draw_access[a] = 0
                astro_ranges [a] = range(-20,-40)
            game_over()


    

    #show score
    show_score()
    show_life()
    pygame.display.update()